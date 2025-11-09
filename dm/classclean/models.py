from django.db import models
from .tools import DataTool
from django.contrib.auth.models import User
import datetime


# 实例化工具类
DT = DataTool()


# Create your models here.
class ClassCleanRecord(models.Model):
    """班级卫生扣分记录模型"""
    # 所属年级及数字表示
    grade = models.CharField(choices=DT.grades, max_length=2)
    grade_num = models.IntegerField(default=0)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5)

    # 时间段（早上/中午）
    tm = models.CharField(choices=(('早上', '早上'), ('中午', '中午')),
                          max_length=2, default='早上')

    # 问题区域
    area = models.CharField(max_length=20, default='未设置', choices=DT.get_choices())

    # 扣分分值
    decrease = models.IntegerField(default=1)

    # 扣分原因
    reason = models.CharField(max_length=50)

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # 记录人
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.class_and_grade


class ClassCleanScore(models.Model):
    """学生会班级卫生扣分模型"""
    # 所属年级及数字表示
    grade = models.CharField(choices=DT.grades, max_length=2)
    grade_num = models.IntegerField(default=0)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5)

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # 卫生评分
    score = models.DecimalField(decimal_places=2, max_digits=3)

    # 卫生问题描述
    desc = models.CharField(max_length=100, blank=True)

    # 检查人姓名及密码
    owner = models.CharField(max_length=8, default='')
    owner_show = models.CharField(max_length=13, default='')
    pwd = models.CharField(max_length=6)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.date_added, self.class_and_grade)

    def update_desc(self, desc_list):
        """根据列表更新问题字符串"""
        self.desc = '；'.join(desc_list)


class OutLookRecord(models.Model):
    """仪容仪表检查记录"""
    # 所属年级及数字表示
    grade = models.CharField(choices=DT.grades, max_length=2)
    grade_num = models.IntegerField(default=0)

    # 所属班级数字表示
    cs = models.IntegerField(choices=tuple(DT.cs_dict.items()))

    # 自动合成年级+班级字符串表示
    class_and_grade = models.CharField(max_length=5)

    # 产生日期
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(default=datetime.datetime.today())

    # 烫发、染发名单记录
    hair_record = models.CharField(max_length=200, blank=True)
    hair_n = models.IntegerField()

    # 佩戴饰品名单记录
    jewelry_record = models.CharField(max_length=200, blank=True)
    jewelry_n = models.IntegerField()

    # 检查人姓名及密码
    owner = models.CharField(max_length=8, default='')
    owner_show = models.CharField(max_length=13, default='')
    pwd = models.CharField(max_length=6)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.date_added, self.class_and_grade)

    def update_hair_record(self, hair_record_list):
        """更新烫发、染发记录"""
        self.hair_record = ','.join(hair_record_list)
        self.hair_n = len(hair_record_list)

    def update_jewelry_record(self, jewelry_record_list):
        """更新佩戴饰品记录"""
        self.jewelry_record = ','.join(jewelry_record_list)
        self.jewelry_n = len(jewelry_record_list)
