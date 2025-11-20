from django.db import models
from .tools import DataTool
import datetime


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class LongLeaveRecord(models.Model):
    """长假记录"""
    # 姓名
    name = models.CharField(max_length=5)

    # 年级与班级
    class_and_grade = models.CharField(max_length=5, choices=DT.get_all_classes())
    grade = models.CharField(max_length=2)
    cs = models.IntegerField()

    # 请假截止日期
    end_date = models.DateField()

    # 请假类型
    tp = models.BooleanField(default=False)

    # 备注
    desc = models.CharField(max_length=100, default='', blank=True)

    # 生成时间
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class ClassInfo(models.Model):
    """班级信息"""
    # 所属日期
    date = models.DateField()

    # 所属年级
    grade = models.CharField(max_length=2, choices=DT.daily_grades)

    # 班级
    cs = models.CharField(max_length=3, choices=DT.get_all_cs())

    # 年级与班级数字表示
    grade_num = models.IntegerField()
    cs_num = models.IntegerField()

    # 自动合成年级班级字符串
    class_and_grade = models.CharField(max_length=5)

    # 应到人数
    total = models.IntegerField()

    # 实到人数
    come = models.IntegerField()

    def __str__(self):
        """返回模型的字符串表示"""
        return self.class_and_grade


class AbsentStudents(models.Model):
    """请假学生"""
    # 姓名
    name = models.CharField(max_length=5)

    # 请假原因
    reason = models.CharField(max_length=20)

    # 所属班级
    class_belong = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class StayTask(models.Model):
    """留宿上报任务"""
    # 日期及日期字符串
    date = models.DateField(default=datetime.date.today())
    date_str = models.CharField(max_length=10)

    # 包含年级
    grade_include = models.CharField(max_length=10)

    # 是否已完成
    done = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.date_str

    def set_date_str(self):
        """根据日期设置字符串"""
        self.date_str = datetime.date.strftime(self.date, '%Y-%m-%d')

    def set_grade_str(self, grade_list):
        """设置包含年级字符串"""
        self.grade_include = ','.join(grade_list)

    def get_grade_list(self):
        """获取年级列表"""
        return self.grade_include.split(',')
