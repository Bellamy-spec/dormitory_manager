from django.db import models
import datetime
from .tools import DataTool
from su_manage.models import get_owners_pwd


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class CMScore(models.Model):
    """学生会宣传部班会评价模型"""
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

    # 三有：有班主任、有课件、有主持人
    head_in = models.BooleanField(default=False)
    have_ppt = models.BooleanField(default=False)
    have_host = models.BooleanField(default=False)

    # 班会主题
    topic = models.CharField(max_length=20)

    # 纪律问题
    desc = models.CharField(max_length=100, blank=True)

    # 纪律扣分
    decrease = models.DecimalField(decimal_places=2, max_digits=3)

    # 总分
    score = models.DecimalField(decimal_places=2, max_digits=3)

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

    def make_show(self):
        """完善检查人显示"""
        opd = get_owners_pwd('03')
        self.owner_show = self.owner + opd[self.owner][1]
