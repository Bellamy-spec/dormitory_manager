"""工具类"""


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

        # 项目管理员
        self.super_users = ['zz106dyc', '李宪伟', '张志云', '常新辉']

        # 班会纪律问题
        self.desc = {
            'd1': '有同学说话、不专心听讲',
            'd2': '有同学做其他科作业',
            'd3': '有同学未穿全身校服',
        }

    @staticmethod
    def str_two(n):
        """两位化数字字符串"""
        if n < 10:
            return '0' + str(n)
        else:
            return str(n)
