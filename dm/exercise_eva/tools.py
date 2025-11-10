# coding=utf-8
"""工具类"""


class DataTool:
    def __init__(self):
        # 班级数字与名称之间的对应
        self.cs_dict = {}
        for i in range(1, 13):
            self.cs_dict[i] = str(i) + '班'

        # 年级
        self.grades = (('高一', '高一'), ('高二', '高二'))
        self.grades_num = {'高一': 1, '高二': 2}
        self.reverse_grade_num = {1: '高一', 2: '高二'}

        # 项目管理员
        self.super_users = ['zz106dyc', '李宪伟', '张志云', '刘明杰', '常新辉']

        # # 可登记短假的学生会成员
        # self.short_abst_loader = ['20260402']

        # 节能问题
        self.desc = {
            'd1': '教室灯未关',
            'd2': '教室空调未关',
            'd3': '教室多媒体未关',
            'd4': '画室灯未关',
            'd5': '画室空调未关',
        }

    def get_gc_choice(self):
        """生成班级字符串选项"""
        gc_list = []
        for grade_tup in self.grades:
            for i in range(1, 13):
                gc = grade_tup[0] + str(i) + '班'
                gc_list.append((gc, gc))
        return tuple(gc_list)

    @staticmethod
    def str_two(n):
        """两位化数字字符串"""
        if n < 10:
            return '0' + str(n)
        else:
            return str(n)
