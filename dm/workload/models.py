from django.db import models
from .tools import DataTool


# 实例化数据类
DT = DataTool()


# Create your models here.
class Task(models.Model):
    """一个月的任务"""
    # 月份
    month = models.CharField(max_length=8, choices=DT.get_months())

    # 周数
    weeks = models.IntegerField(default=0)

    # 所属年级
    grade = models.IntegerField(choices=tuple(DT.grades.items()))
    grade_str = models.CharField(max_length=2)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.month


class WorkloadRecord(models.Model):
    """表示一个老师一个月工作量的记录类"""
    # 教师姓名
    name = models.CharField(max_length=5)

    # 所属月份任务对象
    month = models.ForeignKey(Task, on_delete=models.CASCADE)

    # 所属年级
    grade_num = models.IntegerField(choices=tuple(DT.grades.items()))
    grade = models.CharField(max_length=2, default='')

    # 所教学科
    subject = models.CharField(max_length=5, choices=DT.get_subject_options())

    # 所教班级及班级数量
    # css = models.CharField(max_length=20)
    cs_n = models.IntegerField()
    css_format = models.CharField(max_length=40, default='')

    # 周教案数，周课时数，月教案数，月课时数
    week_plans = models.IntegerField()
    week_lessons = models.IntegerField()
    month_plans = models.IntegerField()
    month_lessons = models.IntegerField()

    # 早辅导次数，晚自习次数
    morning_lessons = models.IntegerField()
    evening_lessons = models.IntegerField()

    # 是否班主任，班级人数
    headteacher = models.BooleanField(default=False)
    headteacher_n = models.IntegerField(default=0)

    # 是否年级长，年级人数
    grade_master = models.BooleanField(default=False)
    grade_master_n = models.IntegerField(default=0)

    # 是否备课组长，备课组人数
    small_master = models.BooleanField(default=False)
    small_master_n = models.IntegerField(default=0)

    # 是否教研组长，教研组人数
    big_master = models.BooleanField(default=False)
    big_master_n = models.IntegerField(default=0)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def get_cs_list(self):
        """生成班级列表"""
        cs_list = self.css_format.split(',')
        return cs_list

    def update_cs(self, cs_list):
        """根据班级列表更新所教班级信息"""
        self.css_format = ','.join(cs_list)
        self.cs_n = len(cs_list)


class SubLesson(models.Model):
    """代课模型"""
    # 被代课教师
    sub_teacher = models.CharField(max_length=5)

    # 代课班级
    sub_class = models.CharField(max_length=5, choices=DT.get_class())

    # 代课时间
    sub_time = models.CharField(max_length=50)

    # 代课节数
    sub_lessons = models.IntegerField(default=0)

    # 所属记录对象
    record_belong = models.ForeignKey(WorkloadRecord, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return '代{}{}'.format(self.sub_teacher, self.sub_class)
