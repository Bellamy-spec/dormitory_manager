from django.db import models
from .tools import DataTool
import random


# 实例化数据类
DT = DataTool()


# Create your models here.
class Program(models.Model):
    """节目类"""
    # 节目名称
    name = models.CharField(max_length=20)

    # 节目表演形式
    tp = models.CharField(max_length=3, choices=DT.tp)

    # 节目负责人姓名
    owner = models.CharField(max_length=5)

    # 负责人所在班级
    owner_class = models.CharField(max_length=5, choices=DT.get_all_classes())

    # 负责人联系方式
    owner_phone = models.CharField(max_length=11)

    # 所需话筒个数
    mac_nums = models.IntegerField(choices=DT.get_mac_nums())

    # 节目简介
    desc = models.TextField()

    # 其他
    etc = models.CharField(max_length=100, default='')

    # 年份
    year = models.CharField(max_length=4, default='2023')

    # 口令
    sec = models.CharField(max_length=6, default='000000')

    def __str__(self):
        """返回模型的字符串表示"""
        return '节目：{}，负责人：{}'.format(self.name, self.owner)

    def update_sec(self):
        """更新口令"""
        new_sec = ''
        for i in range(6):
            new_sec += str(random.randint(0, 9))
        self.sec = new_sec


class Performer(models.Model):
    """表演者类"""
    # 所属节目
    program_belong = models.ForeignKey(Program, on_delete=models.CASCADE)

    # 表演者姓名
    name = models.CharField(max_length=5)

    # 表演者所属班级（或教师）
    class_belong = models.CharField(max_length=5, choices=DT.get_all_include_teacher())

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Costume(models.Model):
    """服装类"""
    # 服装名称
    name = models.CharField(max_length=20)

    # 服装模特
    mt = models.CharField(max_length=5)

    # 模特所属班级（或教师）
    mt_class = models.CharField(max_length=5, choices=DT.get_all_include_teacher())

    # 联络人姓名
    owner = models.CharField(max_length=5)

    # 联络人所属班级
    owner_class = models.CharField(max_length=5, choices=DT.get_all_classes())

    # 联络人联系方式
    owner_phone = models.CharField(max_length=11)

    # 服装简介
    desc = models.TextField()

    # 设计图纸
    drawing = models.ImageField(upload_to='costume/', null=True, blank=True)

    # 编号
    num = models.IntegerField(default=0)

    # 年份
    year = models.CharField(max_length=4, default='2023')

    # 口令
    sec = models.CharField(max_length=6, default='000000')

    def __str__(self):
        """返回模型的字符串表示"""
        return '{}.服装：{}，模特：{}，联络人：{}'.format(self.num, self.name, self.mt, self.owner)

    def update_sec(self):
        """更新口令"""
        new_sec = ''
        for i in range(6):
            new_sec += str(random.randint(0, 9))
        self.sec = new_sec


class Designer(models.Model):
    """表示服装设计师的类"""
    # 所属服装
    costume_belong = models.ForeignKey(Costume, on_delete=models.CASCADE)

    # 设计师姓名
    name = models.CharField(max_length=5)

    # 设计师所属班级
    class_belong = models.CharField(max_length=5, choices=DT.get_all_classes())

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
