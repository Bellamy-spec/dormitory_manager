from django.db import models
from .data import Data
from django.contrib.auth.models import User
from django.utils.timezone import now
from pypinyin import lazy_pinyin

# 实例化数据类
DT = Data()


def get_gender(id_number):
    """根据身份证号返回性别"""
    # 取出倒数第二位数字值
    gender_key = int(id_number[-2])

    # 判断
    if gender_key % 2:
        gender = '男'
    else:
        gender = '女'

    return gender


# Create your models here.
class Record(models.Model):
    """扣分记录"""
    tm = models.CharField(max_length=10, choices=DT.tm, default='午休纪律')
    class_and_grade = models.CharField(max_length=20)
    cs = models.IntegerField(default=0)
    grade = models.IntegerField(choices=DT.grade, default=1)
    dormitory = models.CharField(max_length=5)
    tp = models.CharField(max_length=10, choices=DT.tp, default='卫生')
    decrease = models.IntegerField(default=1)
    reason = models.CharField(max_length=60)
    date_added = models.DateTimeField(auto_now_add=True)

    # 床铺信息
    bed = models.IntegerField(choices=DT.ap, default=0)
    student = models.CharField(max_length=5, blank=True, default='')
    bed_area = models.CharField(max_length=4, default='公共区域')

    # 实际日期
    date = models.DateField(auto_now_add=True)

    # 分组日期
    date_group = models.DateField(default=now())
    date_group_str = models.CharField(max_length=20, default='')

    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=5, choices=DT.dorm_gender, default='boy')

    def __str__(self):
        """返回模型的字符串表示"""
        return self.dormitory


class Investigation(models.Model):
    """满意度调查"""
    # 调查学年
    school_year = models.CharField(max_length=11, choices=DT.get_school_year())

    # 活跃状态
    active = models.BooleanField(default=True)

    # 问卷份数
    total = models.IntegerField(default=0)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.school_year


class Paper(models.Model):
    """问卷类"""
    # 基本情况
    gender = models.CharField(max_length=1, choices=DT.gdc)
    grade = models.IntegerField(choices=DT.grade)
    gc = models.CharField(max_length=5, choices=DT.get_gc())
    dorm = models.CharField(max_length=3, choices=DT.all_dormitory_format())

    # 对应宿管老师，系统根据宿舍号自动对应
    teacher = models.CharField(max_length=5)

    # 问卷题目
    t1 = models.IntegerField(choices=DT.paper_options, default=5)
    t2 = models.IntegerField(choices=DT.paper_options, default=5)
    t3 = models.IntegerField(choices=DT.paper_options, default=5)
    t4 = models.IntegerField(choices=DT.paper_options, default=5)
    t5 = models.IntegerField(choices=DT.paper_options, default=5)
    t6 = models.IntegerField(choices=DT.paper_options, default=5)
    t7 = models.IntegerField(choices=DT.paper_options, default=5)
    t8 = models.IntegerField(choices=DT.paper_options, default=5)
    t9 = models.IntegerField(choices=DT.paper_options, default=5)
    t10 = models.IntegerField(choices=DT.paper_options, default=5)
    t11 = models.IntegerField(choices=DT.paper_options, default=5)
    t12 = models.IntegerField(choices=DT.paper_options, default=5)
    t13 = models.TextField(blank=True)
    t14 = models.TextField(blank=True)

    # 所属调查对象
    inv = models.ForeignKey(Investigation, on_delete=models.CASCADE)

    # 填写时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    # 问卷编号，系统自动生成
    num = models.IntegerField()
    num_name = models.CharField(max_length=8)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.num_name

    def make_num_name(self):
        """生成问卷编号"""
        self.num_name = self.inv.school_year[5:9] + DT.str_four(self.num)


class NewStudent(models.Model):
    """新生类"""
    # 姓名、身份证号
    name = models.CharField(max_length=5)
    id_number = models.CharField(max_length=18, blank=True)

    # 性别
    gender = models.CharField(max_length=2, choices=DT.gender, default='未知')

    # 班级、宿舍、床铺号
    cs = models.IntegerField()
    gc = models.CharField(max_length=8)
    dorm = models.CharField(max_length=8)
    bed = models.IntegerField()

    # 年级
    grade_year = models.IntegerField()
    grade_year_str = models.CharField(max_length=5)

    # 已毕业
    graduated = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.gc, self.name)

    def fill_blank(self):
        """补充完整年级、班级字符串、判断性别"""
        self.grade_year_str = str(self.grade_year) + '级'
        self.gc = self.grade_year_str + DT.str_two(self.cs) + '班'

        if self.id_number:
            self.gender = get_gender(self.id_number)


def get_students(gc, logic=True):
    """以列表形式返回一个班级所有学生"""
    if not logic:
        # 班级字符串转为逻辑班级字符串
        grade = gc[:2]
        lgd = DT.logic_grade[grade]
        cs = gc[2:-1]
        if len(cs) < 2:
            cs = '0' + cs
        gc = lgd + cs + '班'

    student_list = []
    for ob in NewStudent.objects.filter(gc=gc):
        student_list.append(ob.name)

    return sorted(student_list, key=lambda x: ''.join(lazy_pinyin(x)))


def format_gc_students(grades=('高一', '高二', '高三'), logic=True):
    """返回班级学生对应格式化字典"""
    # 初始化存放字典
    gs_dict = {}

    # 三个年级
    for grade in grades:
        # 逻辑年级
        lg = DT.logic_grade[grade]

        # 12个班
        for cs in range(1, 13):
            # 合成班级字符串
            cs_str = DT.str_two(cs)
            gc = lg + cs_str + '班'

            # 加入字典
            if logic:
                gs_dict[gc] = get_students(gc)
            else:
                rgc = grade + str(cs) + '班'
                gs_dict[rgc] = get_students(gc)

    return gs_dict


def all_students(grades=('高一', '高二', '高三')):
    """获取指定年级所有学生列表"""
    # 初始化学生姓名列表
    st_list = []

    for grade in grades:
        # 逻辑年级
        lg = DT.logic_grade[grade]

        # 12个班
        for cs in range(1, 13):
            # 合成班级字符串
            cs_str = DT.str_two(cs)
            gc = lg + cs_str + '班'

            # 加入列表
            st_list += get_students(gc)

    return st_list


def st_gc(grades=('高一', '高二', '高三')):
    """根据学生姓名确定所有可能所在的班级"""
    st_gc_dict = {}
    for lgc, st_list in format_gc_students(grades=grades).items():
        # 逻辑班级字符串转换成正常的班级字符串
        lgd = lgc[:5]
        grade = DT.logic_grade_reverse[lgd]
        cs = int(lgc[5:7])
        gc = grade + str(cs) + '班'

        # 加入字典
        for st in st_list:
            st_gc_dict.setdefault(st, [])
            st_gc_dict[st].append(gc)

    return st_gc_dict


def empty_bed():
    """返回各宿舍空床铺"""
    # 初始化存放字典
    empty_bed_dict = {}

    # 遍历一遍即可完成处理
    for ob in NewStudent.objects.filter(graduated=False):
        # 设置默认值（默认全空）
        empty_bed_dict.setdefault(ob.dorm, sorted(list(range(1, 9)), reverse=True))

        # 去掉有人住的床铺
        empty_bed_dict[ob.dorm].remove(ob.bed)

    return empty_bed_dict


def get_st(dorm, bed):
    """返回指定宿舍、床铺号对应的学生及其班级"""
    # 尝试匹配
    sts = NewStudent.objects.filter(dorm=dorm, bed=bed, graduated=False)
    if sts:
        # 匹配到时的做法
        st, lgc = sts[0].name, sts[0].gc

        # 取得年级
        grade = DT.logic_grade_reverse[lgc[:5]]

        # 匹配班级数字
        cs = DT.num_regex.match(lgc[5:]).group(0)
        cs = str(int(cs))

        # 合成班级字符串
        gc = grade + str(cs) + '班'

        # 返回
        return st, gc
    else:
        # 按原方案返回班级，学生为空
        return '', DT.get_class(dorm)


def get_dorms(grade_year=None):
    """根据学年获取所有宿舍列表"""
    # 读取
    dorm_list = []
    if grade_year is None:
        students = NewStudent.objects.filter(graduated=False)
    else:
        students = NewStudent.objects.filter(grade_year=grade_year, graduated=False)

    for student in students:
        dorm_list.append(student.dorm)

    # 去重、排序
    dorm_list = list(set(dorm_list))
    dorm_list.sort()

    return dorm_list


# def test():
#     """做个测试"""
#     print(format_gc_students())
#
#
# if __name__ == '__main__':
#     test()
