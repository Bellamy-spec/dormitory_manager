from django.db import models
from .tools import DataTool


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class Material(models.Model):
    """素材类"""
    # 标题
    title = models.CharField(max_length=20)

    # 主线
    line = models.CharField(choices=DT.line_name, max_length=7)

    # 简介
    desc = models.TextField(blank=True)

    # 附件
    file = models.FileField(upload_to='math_culture/share/')

    # 上传日期
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title
