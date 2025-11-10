"""一些方便调用的工具类"""
import re


class DataTool:
    def __init__(self):
        # 班级数字与名称之间的对应
        self.cs_dict = {}
        for i in range(1, 13):
            self.cs_dict[i] = str(i) + '班'

        # 年级
        self.grades = (('高一', '高一'), ('高二', '高二'), ('高三', '高三'))
        self.grades_num = {'高一': 1, '高二': 2, '高三': 3}
        self.reverse_grade_num = {1: '高一', 2: '高二', 3: '高三'}

        # 该项目的管理员
        self.managers = ['zz106dyc']

        # 匹配数字
        self.num_regex = re.compile(r'\d+')
