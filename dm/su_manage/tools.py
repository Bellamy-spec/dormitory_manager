"""静态数据类"""
from django.contrib.auth.models import Group


class DataTool:
    def __init__(self):
        # 超级管理员（教师）
        self.super_manager = ['zz106dyc', '李宪伟', '张志云', '常新辉']

        # # 部门分类
        # self.departments = {
        #     '主席团': '01',
        #     '卫生部': '02',
        #     '宣传部': '03',
        #     '文体部': '04',
        #     '纪律部': '05',
        # }
        #
        # # 管理员（师生）
        # self.manager = {
        #     'zz106dyc': list(self.departments.keys()),
        #     '李宪伟': list(self.departments.keys()),
        #     '杨子萱': list(self.departments.keys()),
        #     '秦萌': ['卫生部'],
        #     '宋钰伟': ['宣传部'],
        #     '苏宴': ['文体部'],
        #     '丁子珊': ['纪律部'],
        # }

        # 年级、班级相关参数
        self.grades = ['高一', '高二']
        self.cn = 12

        # 级别对应
        self.level_dict = {0: '干事', 1: '副职', 2: '正职'}
        self.level_dict_reverse = {'干事': 0, '副职': 1, '正职': 2}

        # 干部称呼
        self.hn = (('部长', '(副)部长'), ('主席', '(副)主席'))

        # 学生用户分组
        self.student_group = Group.objects.get(name='Student')

        # 不上早操和课间操的特殊成员
        self.special_member1 = []
        self.special_member2 = ['20260501']

    def all_gc_options(self, simple=False):
        """获得所有班级字符串选项"""
        # 初始化班级选项列表
        gc_list = []

        for grade in self.grades:
            for cs in range(1, self.cn + 1):
                gc = grade + str(cs) + '班'
                if simple:
                    gc_list.append(gc)
                else:
                    gc_list.append((gc, gc))

        return tuple(gc_list)

    @staticmethod
    def str_two(n):
        """数字两位化字符串处理"""
        if n < 10:
            return '0' + str(n)
        else:
            return str(n)
