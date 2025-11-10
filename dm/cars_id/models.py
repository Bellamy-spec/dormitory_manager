from django.db import models
from .tools import DataTool


# 实例化数据类
DT = DataTool()


# Create your models here.
class CarRecord(models.Model):
    """车牌信息类"""
    # 车主姓名
    name = models.CharField(max_length=10)

    # 人员类别
    tp = models.CharField(max_length=5, choices=DT.tp, default=DT.tp[0][0])

    # 手机号
    phone_number = models.CharField(max_length=11)

    # 车牌号1
    car1 = models.CharField(max_length=8)

    # 车1是否新能源
    is_new_energy1 = models.BooleanField()

    # 车牌号2
    car2 = models.CharField(max_length=8, default='')

    # 车2是否新能源
    is_new_energy2 = models.BooleanField()

    # 提交时间
    datetime_added = models.DateTimeField(auto_now_add=True)
