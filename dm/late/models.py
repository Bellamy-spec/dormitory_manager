from django.db import models
from .tools import DataTool
import datetime


# 实力化工具类
DT = DataTool()


# Create your models here.
class DateRecord(models.Model):
    """记录一天的迟到情况"""
    # 发生日期
    date = models.DateField(default=datetime.datetime.today())

    # 日期的字符串表示
    date_str = models.CharField(max_length=10)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.date_str


class ClassRecord(models.Model):
    """记录一个班级的迟到情况"""
    # 发生日期
    date_happened = models.ForeignKey(DateRecord, on_delete=models.CASCADE)

    # 所属年级及数字表示
    grade = models.CharField(choices=DT.grades, max_length=2)
    grade_num = models.IntegerField(default=0)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5)

    # 迟到学生字符串表示
    late_students_am = models.CharField(max_length=200, default='无')
    late_students_pm = models.CharField(max_length=200, default='无')

    # 迟到人次
    late_num = models.IntegerField(default=0)
    has_late = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.class_and_grade


class LateStudent(models.Model):
    """表示单个迟到学生的模型"""
    # 姓名
    name = models.CharField(max_length=10)

    # 迟到时间段
    tm = models.CharField(choices=(('早上', '早上'), ('中午', '中午')), max_length=2)

    # 所属班级
    class_belong = models.ForeignKey(ClassRecord, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
