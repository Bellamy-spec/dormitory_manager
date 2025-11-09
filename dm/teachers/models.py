from django.db import models


# Create your models here.
class Teacher(models.Model):
    """教师类"""
    # 教师姓名
    name = models.CharField(max_length=10)

    # 教师性别
    gender = models.CharField(choices=(('男', '男'), ('女', '女')), max_length=1)

    # 证件类型
    card_type = models.CharField(max_length=5, default='身份证')

    # 证件号码
    id_number = models.CharField(max_length=18)

    # 根据身份证号得出的性别
    gender1 = models.CharField(max_length=1)

    # 提交时间
    datetime_added = models.DateTimeField(auto_now_add=True)
