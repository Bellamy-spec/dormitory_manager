from django.db import models
from .tools import DataTool


# 实例化数据类
DT = DataTool()


# Create your models here.
class BKRecord(models.Model):
    """填报记录"""
    # 姓名
    name = models.CharField(max_length=5)

    # 监考考点
    work_point = models.CharField(max_length=5, choices=DT.point_choices)

    # 身份证号
    id_number = models.CharField(max_length=18)

    # 银行卡号
    bank_id = models.CharField(max_length=19)

    # 所属银行
    bank_tp = models.CharField(max_length=10)

    # 填报时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
