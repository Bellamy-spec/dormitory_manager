# coding=utf-8
"""方便调用的工具类"""
import datetime
import os
from django.http import Http404
from django.conf import settings


class DataTool:
    """静态数据类"""
    def __init__(self):
        # 项目管理员
        self.super_users = ['zz106dyc', '李宪伟']
        self.operators = self.super_users + ['headteacher']

        # 当前年份、月份
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month

        # 起始年月
        self.start_year = self.year - 1
        self.start_month = self.month

        # 选项中学期个数
        self.term_n = 5

        # 年级汉字与数字对应
        self.grades = {'高一': 1, '高二': 2, '高三': 3}
        self.grades_reverse = {1: '高一', 2: '高二', 3: '高三'}

        # 各年级班级数量
        self.grade_csn = {'高一': 12, '高二': 12, '高三': 12}

        # 根路径
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # A4横向尺寸
        self.cert_width = 1754
        self.cert_height = 1240

        # 称呼模板
        self.call_text = ' {} 同学：'

        # 正文模板
        self.text_text = '    在{}中，成绩显著，荣获 {} ，特发此证，以资鼓励。'

        # 落款
        self.down_text = settings.USER_NAME

        # 日期模板
        self.date_text = ' {} 年 {} 月 {} 日'

        # 科目列号对应
        self.subject_idx = {'语文': 3, '数学': 4, '外语': 5, '物理': 6, '化学': 7, '生物': 8, '政治': 9,
                            '地理': 10, '历史': 11, '体育': 12, '美术班名次': 13, '文化班名次': 14}

    def get_current_term(self, ch=False, ym=None):
        """获取学期表示（默认当前）"""
        if ym is None:
            ym = (self.year, self.month)
        if ym[1] < 7:
            if ch:
                return '{}~{}学年第2学期'.format(ym[0] - 1, ym[0])
            else:
                return '{}-{}_2'.format(ym[0] - 1, ym[0])
        else:
            if ch:
                return '{}~{}学年第1学期'.format(ym[0], ym[0] + 1)
            else:
                return '{}-{}_1'.format(ym[0], ym[0] + 1)

    def make_term_choices(self):
        """生成学期选项"""
        # 初始化年月和存放列表
        year = self.start_year
        month = self.start_month
        term_list = []

        for i in range(self.term_n):
            # 生成学期的两种表示并加入列表
            term = self.get_current_term(ym=(year, month))
            term_ch = self.get_current_term(ch=True, ym=(year, month))
            term_list.append((term, term_ch))

            # 年月加6
            month += 6
            if month > 12:
                month -= 12
                year += 1

        return tuple(term_list)

    def make_gc_choices(self):
        """生成班级选项"""
        gc_list = []
        for grade, csn in self.grade_csn.items():
            for cs in range(1, csn + 1):
                gc = grade + str(cs) + '班'
                gc_list.append((gc, gc))
        return tuple(gc_list)

    def check_operator(self, user):
        """检验是否操作员"""
        if user.username not in self.operators:
            return Http404
