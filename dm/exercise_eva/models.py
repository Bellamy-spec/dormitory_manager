# coding=utf-8
from django.db import models
from .tools import DataTool
import datetime
from su_manage.models import get_owners_pwd
from decimal import Decimal

# 实例化静态数据类
DT = DataTool()


# Create your models here.
class ExerciseScore(models.Model):
    """纪律部、文体部课间操评价模型"""
    # TODO:基础信息
    # 所属年级及数字表示
    grade_num = models.IntegerField(default=0)
    grade = models.CharField(choices=DT.grades, max_length=2)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5, choices=DT.get_gc_choice())

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # TODO:系统拉取数据
    # 应跑操人数（不含长期假和不在校的）
    to_come = models.IntegerField()

    # 短假人数
    short_abst = models.IntegerField(default=0)

    # 学生会工作人员人数
    work_abst = models.IntegerField(default=0)

    # TODO:学生会上传数据
    # 质量分
    quality_score = models.DecimalField(decimal_places=2, max_digits=3)

    # 实到人数
    act_come = models.IntegerField()

    # 迟到和未穿校服人数
    late_come = models.IntegerField(default=0)
    no_wear = models.IntegerField(default=0)

    # TODO:系统计算
    # 旷操人数 = 应跑操人数 - 短假人数 - 学生会工作人员人数 - 实到人数
    escape = models.IntegerField(default=0)

    # 总分 = 质量分 - 旷操人数 - （迟到人数 + 未校服人数） * 0.1
    total_score = models.DecimalField(decimal_places=2, max_digits=3)

    # TODO:操作权限验证
    # 检查人姓名及密码
    owner = models.CharField(max_length=8, default='')
    owner_show = models.CharField(max_length=13, default='')
    pwd = models.CharField(max_length=6)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.date_added, self.class_and_grade)

    def make_gc(self):
        """合成班级字符串"""
        self.class_and_grade = self.grade + str(self.cs) + '班'

    def make_show(self):
        """完善检查人显示"""
        if self.owner:
            opd = {**get_owners_pwd('04'), **get_owners_pwd('05'), **get_owners_pwd('01')}
            self.owner_show = self.owner + opd[self.owner][1]

    def gc_fill(self):
        """根据班级字符串补全班级、年级信息"""
        self.grade = self.class_and_grade[:2]
        self.grade_num = DT.grades_num[self.grade]
        self.cs = int(self.class_and_grade[2:-1])

    def calculate_score(self):
        """计算旷操人数和课间操评价总分"""
        self.escape = self.to_come - self.act_come - self.short_abst - self.work_abst
        if self.escape < 0:
            # 不存在旷操人数为负的情况
            self.escape = 0
        self.total_score = self.quality_score - Decimal(self.escape) \
                           - Decimal((self.late_come + self.no_wear) * 0.1)


class ShortAbst(models.Model):
    """短假学生登记"""
    # 所属年级及数字表示
    grade_num = models.IntegerField(default=0)
    grade = models.CharField(choices=DT.grades, max_length=2)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5, choices=DT.get_gc_choice())

    # 姓名
    name = models.CharField(max_length=5)

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # 检查人姓名及密码
    owner = models.CharField(max_length=8, default='', blank=True)
    owner_show = models.CharField(max_length=13, default='')
    pwd = models.CharField(max_length=6, blank=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {} {}'.format(self.date_added, self.class_and_grade, self.name)

    def make_gc(self):
        """合成班级字符串"""
        self.class_and_grade = self.grade + str(self.cs) + '班'

    def make_show(self):
        """完善检查人显示"""
        if self.owner:
            opd = {**get_owners_pwd('04'), **get_owners_pwd('05'), **get_owners_pwd('01')}
            self.owner_show = self.owner + opd[self.owner][1]

    def gc_fill(self):
        """根据班级字符串补全班级、年级信息"""
        self.grade = self.class_and_grade[:2]
        self.grade_num = DT.grades_num[self.grade]
        self.cs = int(self.class_and_grade[2:-1])


class ECOScore(models.Model):
    """节能记录"""
    # 所属年级及数字表示
    grade_num = models.IntegerField(default=0)
    grade = models.CharField(choices=DT.grades, max_length=2)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5, choices=DT.get_gc_choice())

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # 节能问题描述
    desc = models.CharField(max_length=100, blank=True)

    # 检查人姓名及密码
    owner = models.CharField(max_length=8, default='', blank=True)
    owner_show = models.CharField(max_length=13, default='')
    pwd = models.CharField(max_length=6, blank=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.date_added, self.class_and_grade)

    def make_gc(self):
        """合成班级字符串"""
        self.class_and_grade = self.grade + str(self.cs) + '班'

    def make_show(self):
        """完善检查人显示"""
        if self.owner:
            opd = {**get_owners_pwd('04'), **get_owners_pwd('05'), **get_owners_pwd('01')}
            self.owner_show = self.owner + opd[self.owner][1]

    def gc_fill(self):
        """根据班级字符串补全班级、年级信息"""
        self.grade = self.class_and_grade[:2]
        self.grade_num = DT.grades_num[self.grade]
        self.cs = int(self.class_and_grade[2:-1])

    def update_desc(self, desc_list):
        """根据列表更新问题字符串"""
        self.desc = '；'.join(desc_list)
