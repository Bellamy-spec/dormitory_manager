"""一些方便调用的工具"""
import re


class DataTool:
    """数据工具类"""
    def __init__(self):
        """初始化类的属性"""
        # 年级与数字对应关系字典
        self.grade_num = {'高一': 1, '高二': 2, '高三': 3}

        # 匹配数字
        self.num_regex = re.compile(r'\d+')

        # 此项目的管理员
        self.super_users = ['李宪伟', 'zz106dyc']

        # 可以操作上报数据的用户
        self.operators = self.super_users + ['headteacher']

    def get_class_num(self, cs):
        """根据班级名称得出年级班级数字二元组"""
        cs_num = int(self.num_regex.findall(cs)[0])
        return self.grade_num[cs[:2]], cs_num
