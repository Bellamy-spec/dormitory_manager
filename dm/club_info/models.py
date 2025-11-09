from django.db import models
from .tools import DataTool


# 实例化数据类
DT = DataTool()


# Create your models here.
class Club(models.Model):
    """表示社团的类"""
    # 社团名称
    name = models.CharField(max_length=20)

    # 社团简介
    desc = models.CharField(max_length=100)

    # 社团学生人数
    nums = models.IntegerField(default=0)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Member(models.Model):
    """表示社团成员的类"""
    # 所属社团
    club_belong = models.ForeignKey(Club, on_delete=models.CASCADE)

    # 姓名
    name = models.CharField(max_length=5)

    # 身份证号
    id_number = models.CharField(max_length=18)

    # 角色
    tp = models.CharField(max_length=4, choices=DT.tp)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
