"""静态数据类"""
import re


class DataTool:
    def __init__(self):
        # 年级列表
        self.grades = ['高一', '高二']

        # 年级与数字对应
        self.grades_dict = {'高一': 1, '高二': 2, '高三': 3}
        self.grades_dict_reverse = {1: '高一', 2: '高二', 3: '高三'}

        # 班级数字列表(1~12)
        self.css = list(range(1, 13))

        # 匹配数字
        self.num_regex = re.compile(r'\d+')

        # 项目管理员
        self.managers = ['zz106dyc', '刘明杰', '李宪伟']

        # 项目操作人员
        self.operators = self.managers + ['headteacher']

        # 每日请假与在校上报系统的年级
        self.daily_grades = (('高一', '高一'), ('高二', '高二'), ('高三', '高三'))

        # 两操请假类型
        self.tp = (
            ('早操和课间操', '早操和课间操'),
            ('仅早操', '仅早操'),
            ('仅课间操', '仅课间操'),
        )

    def get_all_classes(self):
        """返回所有年级班级字符串元组"""
        gc_list = []
        for grade in self.grades:
            for cs in self.css:
                gc = grade + str(cs) + '班'
                gc_list.append((gc, gc))
        return tuple(gc_list)

    def get_all_cs(self):
        """返回所有班级列表（不分年级）"""
        cs_list = []
        for cs in self.css:
            cs_list.append((str(cs) + '班', str(cs) + '班'))

        # 添加13班
        cs_list.append(('13班', '13班'))

        return tuple(cs_list)

    @staticmethod
    def get_grade(gc):
        """根据给定年级班级字符串返回年级"""
        return gc[:2]

    def get_cs(self, gc):
        """根据给定年级班级字符串返回班级数字"""
        return int(self.num_regex.findall(gc)[0])

    def get_cs_dict(self):
        """获取班级与字符串对应字典"""
        cs_dict = {}
        for grade in ['高一', '高二', '高三']:
            for cs in range(1, 13):
                gc = grade + str(cs) + '班'
                gc_str = str(self.grades_dict[grade]) + '-' + str(cs)
                cs_dict[gc] = gc_str

        # 加入高三13班
        cs_dict['高三13班'] = '3-13'

        return cs_dict

    def get_reverse_cs_dict(self):
        """班级与字符串对应反字典"""
        cs_dict = self.get_cs_dict()
        return dict(zip(cs_dict.values(), cs_dict.keys()))
