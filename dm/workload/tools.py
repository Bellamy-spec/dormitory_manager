"""方便随时调用的工具类"""
import datetime
import re


class DataTool:
    """静态数据类"""
    def __init__(self):
        # 项目管理员
        self.managers = ['zz106dyc', '陈政', '高一年级长', '高二年级长', '高三年级长']
        self.manager_areas = {
            'zz106dyc': [1, 2, 3],
            '陈政': [1, 2, 3],
            '高一年级长': [1],
            '高二年级长': [2],
            '高三年级长': [3],
        }

        # 最多允许填写近六个月的记录
        self.max_months = 6

        # 年级
        self.grades = {1: '高一', 2: '高二', 3: '高三'}
        self.reverse_grades = {'高一': 1, '高二': 2, '高三': 3}

        # 学科
        self.subjects = ['语文', '数学', '外语', '政治', '历史', '地理', '物理', '化学',
                         '生物', '美术', '体育与健康', '音乐', '心理', '信息技术']

        # 匹配数字
        self.num_regex = re.compile(r'\d+')

        # 最大班号
        self.max_class = 12

    def get_months(self):
        """生成月份选项"""
        # 获取今天日期，年月
        dt = datetime.date.today()
        ym = [dt.year, dt.month]

        # 添加选项
        ym_list = []
        for i in range(self.max_months):
            ym_str = '{}年{}月'.format(*ym)
            ym_str_back = datetime.date.strftime(datetime.date(ym[0], ym[1], 1), '%Y-%m')
            ym_list.append((ym_str_back, ym_str))

            # 月份减1
            if ym[1] > 1:
                ym[1] -= 1
            else:
                ym[0] -= 1
                ym[1] = 12

        return tuple(ym_list)

    def get_subject_options(self):
        """生成学科选项"""
        subject_list = []
        for subject in self.subjects:
            subject_list.append((subject, subject))
        return tuple(subject_list)

    def get_class(self):
        """生成三个年级的班级选项"""
        class_list = []
        for grade_str in self.reverse_grades.keys():
            for cs in range(1, self.max_class + 1):
                gc = grade_str + str(cs) + '班'
                class_list.append((gc, gc))
        return tuple(class_list)
