from django.db import models
import datetime
from django.contrib.auth.models import User
from .tools import DataTool
import random
from django.core.exceptions import ObjectDoesNotExist


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class SchoolYear(models.Model):
    """届别"""
    # 起始日期，创建时设置
    start_date = models.DateField(default=datetime.date.today())

    # 结束日期，创建时设置，年份须为起始日期加1
    end_date = models.DateField()

    # 名称，自动合成
    name = models.CharField(max_length=11)

    # 是否当前，自动判断
    current = models.BooleanField(default=False)

    # 代号，自动生成，同结束日期年份+1
    code = models.CharField(max_length=4)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def fill_blank(self):
        """补充完整自动生成的属性"""
        self.name = '{}~{}学年'.format(self.start_date.year, self.end_date.year)
        self.code = str(self.end_date.year + 1)
        self.config_current()

    def config_current(self):
        """判断是否当前学年"""
        # 判断是否已存在其他当前学年
        have_current = False
        for sy in SchoolYear.objects.filter(current=True):
            if sy != self:
                have_current = True

        # 同时满足时间条件和无其他当前学年方可判断为当前学年
        if self.start_date <= datetime.date.today() <= self.end_date and not have_current:
            self.current = True
        else:
            self.current = False


class Department(models.Model):
    """部门"""
    # 部门名称（添加时设置）
    name = models.CharField(max_length=5)

    # 部门描述（后期维护）
    desc = models.TextField(blank=True)

    # 部门负责人（超级管理员后期维护）
    master = models.CharField(max_length=70, blank=True, default='')
    master_str = models.CharField(max_length=70, blank=True, default='')

    # 部门代号（添加时设置）
    code_int = models.IntegerField(default=0)
    code = models.CharField(max_length=2)

    # 固定工作时段（work_abst1为早操，work_abst2为课间操，超级管理员设置）
    # work_abst1 = models.BooleanField(default=False)
    work_abst2 = models.BooleanField(default=False)

    # 干部称呼（超级管理员设置）
    head_name = models.CharField(max_length=2, choices=DT.hn)

    # 启用状态
    active = models.BooleanField(default=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def make_code(self):
        """生成代号"""
        self.code = DT.str_two(self.code_int)

    def master_list(self):
        """返回负责人用户对象列表"""
        # 初始化存放列表
        ml = []

        # 获取用户姓名列表
        un_list = self.master.split(',')

        # 用户名转为用户对象存入列表
        for un in un_list:
            try:
                user = StudentUser.objects.get(username=un)
            except ObjectDoesNotExist:
                pass
            else:
                ml.append(user)

        return ml

    def config_master(self, ml):
        """根据用户对象列表设置负责人相关的两个字段"""
        un_list, us_list = [], []
        for user in ml:
            un_list.append(user.username)
            us_list.append(user.username + user.last_name)
        self.master = ','.join(un_list)
        self.master_str = ','.join(us_list)

    def add_master(self, user):
        """添加负责人"""
        ml = self.master_list()
        if len(ml) < 5:
            # 未达到负责人人数上限
            ml.append(user)
            self.config_master(ml)

    def del_master(self, user):
        """删除负责人"""
        ml = self.master_list()
        try:
            ml.remove(user)
        except ValueError:
            # 未找到，已不在，过
            pass
        self.config_master(ml)


class Member(models.Model):
    """成员"""
    # 序号、姓名、班级、所属部门、级别、所属学年、序号基础信息
    num = models.IntegerField()
    name = models.CharField(max_length=5)
    class_and_grade = models.CharField(max_length=5, choices=DT.all_gc_options())
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level = models.IntegerField(default=0, choices=tuple(DT.level_dict.items()))
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    # 主要工作职责（负责人完善，work_abst1，work_abst2意义同上）
    main_work = models.CharField(max_length=100, blank=True)
    # work_abst1 = models.BooleanField(default=False)
    work_abst2 = models.BooleanField(default=False)

    # 称呼、代号（系统合成）
    call = models.CharField(max_length=9)
    code = models.CharField(max_length=8)

    # 检查码（随机六位）
    pwd = models.CharField(max_length=6, default='000000')

    # 账号信息
    user_info = models.CharField(max_length=10, blank=True, default='')

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def fill_blank(self):
        """补充完整称呼和代号"""
        # 级别称呼
        if self.level == 0:
            level_str = '干事'
        elif self.level == 1:
            level_str = '副' + self.department.head_name
        elif self.level == 2:
            level_str = self.department.head_name
        else:
            level_str = ''

        # 合成完整称呼
        self.call = self.department.name + level_str

        # 合成代号
        member_code = DT.str_two(self.num)
        self.code = self.school_year.code + self.department.code + member_code

    def update_pwd(self):
        """更新检查码"""
        # 初始化新密码
        new_pwd = ''

        # 随机生成六次整数随机数
        for i in range(6):
            new_pwd += str(random.randint(0, 9))

        # 更改
        self.pwd = new_pwd

    def config_user(self):
        """生成账号信息"""
        try:
            user = StudentUser.objects.filter(mem=self)[0]
        except IndexError:
            # 无账号信息
            self.user_info = ''
        else:
            # 匹配到账号，进行赋值
            self.user_info = '存在账号：{}'.format(user.username)


class StudentUser(User):
    """学生用户"""
    # 用户关联学生会成员
    mem = models.ForeignKey(Member, on_delete=models.CASCADE)

    def add_student_group(self):
        """加入学生分组"""
        self.groups.add(DT.student_group)

    def set_last_name(self):
        """设置姓名属性"""
        self.last_name = self.mem.name


def get_owners_pwd(dc):
    """取得当届某部所有成员代号-检查码对应关系字典"""
    try:
        # 取得当前学年
        csy = SchoolYear.objects.filter(current=True)[0]
    except IndexError:
        # 未匹配到时，返回空字典
        return {}

    # 取得部门对象
    department = Department.objects.get(code=dc)

    # 初始化存放字典
    opd = {}

    # 加入
    for member in Member.objects.filter(school_year=csy, department=department):
        opd[member.code] = (member.pwd, member.name)

    # 返回
    return opd
