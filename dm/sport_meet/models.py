from django.db import models
from .tools import DataTool
import random


# 实例化数据类
DT = DataTool()


# Create your models here.
class Athletes(models.Model):
    """运动员类"""
    # 姓名
    name = models.CharField(max_length=5)

    # 性别
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))

    # 班级字符串
    class_and_grade = models.CharField(max_length=5, choices=DT.get_class())

    # 年级
    grade_num = models.IntegerField(choices=tuple(DT.grades.items()))
    grade_str = models.CharField(max_length=2, choices=DT.grades_tuple)

    # 班级数字
    cs = models.IntegerField(choices=DT.get_cs())

    # 参与项目
    items = models.CharField(max_length=17, default='')

    # 参与项目数量
    n = models.IntegerField(default=0)

    # 生成编号
    num = models.CharField(max_length=4)

    # 生成运动员口令
    pwd = models.CharField(max_length=6, default='000000')

    # 年份
    year = models.CharField(max_length=4, default='2023')

    def complete(self):
        """根据运动员班级字符串完善年级与班级信息"""
        self.grade_str = self.class_and_grade[:2]
        self.grade_num = DT.grades_reverse[self.grade_str]

        # 匹配班级数字
        self.cs = int(DT.num_regex.findall(self.class_and_grade)[0])

    def str_to_list(self):
        """以列表形式返回参与项目"""
        if self.items:
            return str(self.items).split(',')
        else:
            return []

    def update_items(self, lis):
        """更新参与项目"""
        if lis:
            self.items = ','.join(lis)
        else:
            self.items = ''

    def add_item(self, item):
        """添加运动项目"""
        item_list = self.str_to_list()
        item_list.append(item)
        self.update_items(item_list)

        # 项目数加一
        self.n += 1

    def delete_item(self, item):
        """删除运动项目"""
        item_list = self.str_to_list()
        if item in item_list:
            item_list.remove(item)
            self.update_items(item_list)

            # 项目数减一
            self.n -= 1

    def update_pwd(self):
        """更新运动员口令"""
        # 初始化口令字符串
        pwd_str = ''

        # 生成6位数字口令密码
        for i in range(6):
            pwd_str += str(random.randint(0, 9))

        self.pwd = pwd_str

    def format_items(self):
        """返回(项目,索引)"""
        # 格式化项目列表
        items = []
        for item in self.str_to_list():
            items.append((item, DT.get_item_idx()[item]))

        # 返回元组
        return tuple(items)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{}{}'.format(self.num, self.name)


class PutName(models.Model):
    """报名类"""
    # 姓名
    name = models.CharField(max_length=5)

    # 性别
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))

    # 班级字符串
    class_and_grade = models.CharField(max_length=5, choices=DT.get_class())

    # 报名项目
    item = models.CharField(max_length=5, choices=DT.get_item_tuple())

    # 报名时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    # 所属运动员对象
    athlete_belong = models.ForeignKey(Athletes, on_delete=models.CASCADE)

    # 年份
    year = models.CharField(max_length=4, default='2023')

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.name, self.item)
