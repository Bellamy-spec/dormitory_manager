from django.db import models
from .tools import DataTool
import datetime
from django.contrib.auth.models import User


# 实例化数据类
DT = DataTool()


# Create your models here.
class Activities(models.Model):
    """活动类"""
    # 活动名称
    name = models.CharField(max_length=20)

    # 适用于前端datetime-local格式的日期字符串
    tm_str = models.CharField(
        max_length=16,
        default=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%dT%H:%M'),
    )

    # 活动时间
    tm = models.DateTimeField()

    # 活动地点
    place = models.CharField(max_length=50)

    # 活动简介
    desc = models.CharField(max_length=200)

    # 活动参与人数
    num = models.IntegerField(default=0)

    # 是否正在进行中，可由管理员手动控制
    active = models.BooleanField(default=True)

    # 是否已过时
    out_of_date = models.BooleanField(default=False)

    # 发布时间
    date_added = models.DateTimeField(auto_now_add=True)

    # 发布者
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Participant(models.Model):
    """表示参与者的类"""
    # 所属活动
    activity_belong = models.ForeignKey(Activities, on_delete=models.CASCADE)

    # 参与者姓名
    name = models.CharField(max_length=5)

    # 所属部门
    department = models.CharField(max_length=2, choices=DT.departments)

    # 联系电话
    phone_number = models.CharField(max_length=11)

    # 报名时间
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
