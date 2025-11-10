"""存放动态数据"""
import re
import pytz
import datetime
from . import models
from pypinyin import lazy_pinyin
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Data:
    """数据类"""

    def __init__(self):
        """初始化"""
        self.tp = (
            ('卫生', '卫生'),
            ('说话', '说话'),
            ('迟到', '迟到'),
            ('旷寝', '旷寝'),
            ('外出', '外出'),
            ('未出操', '未出操'),
            ('未关灯', '未关灯'),
        )

        # 与扣分数值建立对应
        self.decrease = {
            '卫生': 1,
            '说话': 1,
            '迟到': 1,
            '旷寝': 5,
            '外出': 1,
            '未出操': 1,
            '未关灯': 1,
        }

        self.tm = (
            ('1午休纪律', '午休纪律'),
            ('2下午内务', '下午内务'),
            ('3晚休纪律', '晚休纪律'),
            ('4早上内务', '早上内务'),
        )

        # 宿管员与负责范围对应
        self.area = {
            '朱天风': '高一男寝',
            '张莲花': '高二男寝',
            '张红': '高三男寝',
            '王苹': '高二女寝2',
            '谢顺芹': '高三女寝1',
            '梁艺': '高一女寝1',
            '王炜敏': '高三女寝2',
            '尚秀枝': '高二女寝1',
            '廉银香': '高一女寝2',
        }

        # 宿管老师列表
        self.teacher_list = ['雷勤', '张莲花', '张红', '张连红', '苏月兰', '谢顺芹', '梁艺',
                             '王炜敏', '尚秀枝', '廉银香', ]

        # 宿管员与负责宿舍性别对应
        self.teacher_gender = {
            # 男生宿管
            '雷勤': 'boy',
            '张莲花': 'boy',
            '张红': 'boy',

            # 女生宿管
            '苏月兰': 'girl',
            '谢顺芹': 'girl',
            '梁艺': 'girl',
            '王炜敏': 'girl',
            '尚秀枝': 'girl',
            '廉银香': 'girl',
            '王海燕': 'girl',
            '魏艳玲': 'girl',
            '张连红': 'girl',
        }
        self.dorm_gender = (('boy', 'boy'), ('girl', 'girl'))
        self.gdc = (('男', '男'), ('女', '女'))
        self.gender_ec = {'boy': '男', 'girl': '女'}

        # # 宿舍号与宿管员、班级对应
        # self.dorm = {
        #     # 男生
        #     '雷勤': [],
        #     '张莲花': [
        #         '351', '360', '362', '353', '364', '366', '368', '355', '357', '370',
        #         '372', '359', '361', '374', '376', '453', '455', '457', '459', '461',
        #     ],
        #     '张红': [
        #         '451', '460', '462', '464', '466', '468', '470', '472', '474', '476',
        #         '553', '555', '557', '559', '576', '561',
        #     ],
        #     '张连红': [
        #         '653', '662', '664', '666', '672', '674', '655', '657', '659', '661',
        #         '668', '670', '676', '574', '566', '568', '562', '564', '570', '572',
        #     ],
        #     # 女生
        #     '苏月兰': [
        #         '660', '651', '633', '652', '654', '656', '658', '629', '627', '625',
        #         '624', '622', '623', '621', '618', '616', '614', '619', '617', '615',
        #         '612', '610', '613', '611', '609', '607', '606', '603', '604', '602',
        #         '601', '608', '620', '631',
        #     ],
        #     '谢顺芹': [
        #         '261', '259', '274', '272', '270', '276', '255', '253', '268', '266',
        #         '264', '262', '251', '260', '258', '233', '252', '254', '256', '231',
        #         '257',
        #     ],
        #     '梁艺': [
        #         '229', '220', '222', '225', '227', '223', '224', '216', '218', '214',
        #         '219', '221', '212', '210', '217', '213', '215', '211', '206', '207',
        #         '209', '208', '201', '205', '203', '202', '204', '118', '120', '122',
        #         '124',
        #     ],
        #     '王炜敏': [
        #         '454', '456', '458', '452', '431', '433', '424', '427', '429', '420',
        #         '418', '421', '423', '425', '414', '412', '410', '415', '417', '419',
        #         '408', '406', '407', '409', '411', '413', '405', '404', '402', '403',
        #         '401', '422', '416',
        #     ],
        #     '尚秀枝': [
        #         '512', '517', '519', '523', '518', '516', '521', '514', '529', '527',
        #         '522', '520', '525', '524', '531', '533', '552', '554', '560', '551',
        #         '556', '558', '502', '504', '501', '503', '505', '511', '508', '506',
        #         '515', '510', '513', '509', '507',
        #     ],
        #     '廉银香': [
        #         '323', '325', '320', '322', '327', '319', '314', '316', '321', '312',
        #         '317', '310', '315', '313', '309', '308', '307', '306', '311', '333',
        #         '352', '354', '356', '358', '318', '329', '324', '331', '301', '305',
        #         '304', '302', '303',
        #     ],
        # }

        # 管理员账号
        self.manager = ['zz106dyc', '李宪伟', '刘明杰']

        # 年级
        self.grade = ((1, '高一'), (2, '高二'), (3, '高三'))
        self.grade_dict = {1: '高一', 2: '高二', 3: '高三'}
        self.grade_dict_reverse = {'高一': 1, '高二': 2, '高三': 3}

        # 匹配数字
        self.num_regex = re.compile(r'\d+')

        # 时区指定为西一区
        self.tz = pytz.timezone('Etc/GMT+1')

        # # 换宿舍
        # self.change_dorm_2 = {
        #     # boys
        #     '451': '351',
        #     '460': '360',
        #     '462': '362',
        #     '453': '353',
        #     '464': '364',
        #     '466': '366',
        #     '468': '368',
        #     '455': '355',
        #     '457': '357',
        #     '470': '370',
        #     '472': '372',
        #     '459': '359',
        #     '461': '361',
        #     '474': '374',
        #     '576': '376',
        #     '553': '453',
        #     '555': '455',
        #     '557': '457',
        #     '559': '459',
        #     '561': '461',
        #
        #     # girls
        #     '452': '352',
        #     '454': '354',
        #     '456': '356',
        #     '458': '358',
        #     '429': '201',
        #     '431': '205',
        #     '422': '203',
        #     '424': '202',
        #     '433': '204',
        #     '423': '211',
        #     '425': '206',
        #     '418': '207',
        #     '420': '209',
        #     '427': '208',
        #     '419': '212',
        #     '421': '210',
        #     '417': '217',
        #     '414': '213',
        #     '416': '215',
        #     '413': '216',
        #     '415': '218',
        #     '412': '214',
        #     '408': '219',
        #     '410': '221',
        #     '411': '224',
        #     '404': '220',
        #     '405': '222',
        #     '407': '225',
        #     '409': '227',
        #     '406': '223',
        #     '401': '229',
        #     '402': '333',
        #     '507': '329',
        #     '509': '324',
        #     '511': '331',
        #     '256': '322',
        #     '252': '325',
        #     '254': '320',
        #     '258': '327',
        #     '251': '323',
        #     '253': '319',
        #     '260': '314',
        #     '262': '316',
        #     '264': '321',
        #     '403': '318',
        #     '270': '312',
        #     '257': '317',
        #     '268': '310',
        #     '255': '315',
        #     '266': '313',
        #     '259': '309',
        #     '276': '308',
        #     '261': '307',
        #     '274': '306',
        #     '272': '311',
        #     '502': '301',
        #     '505': '305',
        #     '503': '304',
        #     '501': '302',
        #     '504': '303',
        # }
        # self.change_dorm_1 = {
        #     # boys
        #     '662': '451',
        #     '664': '460',
        #     '666': '462',
        #     '653': '464',
        #     '668': '466',
        #     '655': '468',
        #     '657': '470',
        #     '659': '472',
        #     '661': '474',
        #     '670': '476',
        #     '672': '553',
        #     '674': '555',
        #     '676': '557',
        #     '570': '559',
        #     '572': '561',
        #     '574': '576',
        #
        #     # girls
        #     '506': '261',
        #     '508': '259',
        #     '510': '257',
        #     '512': '276',
        #     '513': '274',
        #     '515': '272',
        #     '514': '255',
        #     '516': '253',
        #     '517': '270',
        #     '519': '268',
        #     '521': '266',
        #     '518': '264',
        #     '520': '262',
        #     '522': '251',
        #     '523': '260',
        #     '525': '258',
        #     '524': '233',
        #     '529': '252',
        #     '531': '254',
        #     '533': '256',
        #     '552': '231',
        #     '551': '510',
        #     '554': '508',
        #     '556': '506',
        #     '558': '515',
        #     '560': '513',
        #     '154': '511',
        #     '118': '502',
        #     '120': '504',
        #     '122': '501',
        #     '124': '503',
        #     '152': '505',
        #     '527': '509',
        #     '604': '507',
        #     '656': '458',
        #     '658': '456',
        #     '660': '454',
        #     '651': '452',
        #     '652': '433',
        #     '654': '431',
        #     '629': '429',
        #     '631': '427',
        #     '633': '424',
        #     '618': '425',
        #     '620': '423',
        #     '622': '421',
        #     '623': '418',
        #     '625': '420',
        #     '612': '419',
        #     '614': '417',
        #     '616': '415',
        #     '617': '410',
        #     '619': '412',
        #     '621': '414',
        #     '606': '413',
        #     '608': '411',
        #     '610': '409',
        #     '611': '407',
        #     '613': '406',
        #     '615': '408',
        #     '601': '401',
        #     '602': '403',
        #     '603': '402',
        #     '607': '404',
        #     '609': '405',
        #     '627': '416',
        #     '624': '422',
        # }

        # 是否在搬宿舍到下一学年期间
        self.change_dorm = True

        # 问卷选项
        self.paper_options = (
            (5, '非常满意'),
            (4, '满意'),
            (3, '一般'),
            (2, '不满意'),
            (1, '极不满意'),
        )

        # 问卷题目
        self.paper_t = {
            'gender': '*您的性别？',
            'grade': '*您的年级？',
            'gc': '*您的班级？',
            'dorm': '*您的寝室房间号？',
            't1': '*您对宿舍管理老师的工作总体是否满意？',
            't2': '*您对宿舍管理老师的工作态度和责任心是否满意？',
            't3': '*您对宿舍管理老师的管理水平是否满意？',
            't4': '*您有困难时能否及时找到宿管老师？',
            't5': '*宿管老师在工作期间是否经常不定时地在各楼层巡视？',
            't6': '*宿管老师是否能及时发现违纪情况并及时处理？',
            't7': '*您对宿舍的整体环境是否满意？',
            't8': '*您对宿舍的公共卫生情况是否满意？',
            't9': '*您对本宿舍的内部卫生情况是否满意？',
            't10': '*您对宿舍的公共就寝纪律是否满意？',
            't11': '*您对本宿舍的内部就寝纪律是否满意？',
            't12': '*您对宿舍的管理制度是否满意？',
            't13': '您对宿舍管理方面的意见和建议？',
            't14': '您的其他意见和建议？',
        }

        # 单选评价项目
        self.sel_items = [
            '工作总体评分',
            '工作态度和责任心评分',
            '管理水平评分',
            '学生有困难时能及时找到',
            '工作期间经常不定时巡视楼层',
            '能及时发现违纪情况并处理',
            '宿舍整体环境评分',
            '宿舍公共卫生评分',
            '宿舍内部卫生评分',
            '宿舍公共就寝纪律评分',
            '宿舍内部就寝纪律评分',
            '宿舍管理制度评分',
        ]

        # 特殊身份证号
        self.special_id = ['S242293(1)']

        # 性别
        self.gender = (('男', '男'), ('女', '女'), ('未知', '未知'))

        # 逻辑年级对应
        self.logic_grade = {'高一': '2025级', '高二': '2024级', '高三': '2023级'}
        self.logic_grade_reverse = {'2025级': '高一', '2024级': '高二', '2023级': '高三'}

        # 问题区域
        self.ap = (
            (0, '公共区域'),
            (1, '1号床'),
            (2, '2号床'),
            (3, '3号床'),
            (4, '4号床'),
            (5, '5号床'),
            (6, '6号床'),
            (7, '7号床'),
            (8, '8号床'),
        )

        # 录入新生的年级数字
        self.nst_grade = [1, 2, 3]

        # 记录开始显示的日期
        self.start_date = datetime.date(2024, 8, 1)

        # 开放查询
        self.can_que = True
        self.que_start_time = datetime.datetime(2025, 8, 16, 6, 0)

        # 运行着的无头浏览器，默认不打开
        self.b = None
        # self.refresh_browser()

        # 当前验证码字符串
        self.current_captcha_str = ''

    @staticmethod
    def dorm():
        """获取宿舍管理权限"""
        # 确保服务器上进入正确的目录，可正常运行
        if os.name != 'nt':
            os.chdir('/root/dormitory_manager/dm')

        with open('media/dorm_manager.json', encoding='gbk') as f:
            return json.loads(f.read())

    def all_dormitory(self, gender=None):
        """根据宿管权限获取所有宿舍号"""
        dorms = []
        if gender is None:
            for ar in self.dorm().values():
                dorms += ar
        elif gender == 'boy':
            for tm, ar in self.dorm().items():
                if self.teacher_gender[tm] == 'boy':
                    dorms += ar
        elif gender == 'girl':
            for tm, ar in self.dorm().items():
                if self.teacher_gender[tm] == 'girl':
                    dorms += ar
        return sorted(dorms)

    @staticmethod
    def get_all_dormitory(gender=None):
        """根据学生入住情况获取所有宿舍号"""
        dorms = []
        if gender is None:
            students = models.NewStudent.objects.filter(graduated=False)
        elif gender == 'boy':
            students = models.NewStudent.objects.filter(graduated=False, gender='男')
        elif gender == 'girl':
            students = models.NewStudent.objects.filter(graduated=False, gender='女')
        else:
            return

        for student in students:
            if student.dorm not in dorms:
                dorms.append(student.dorm)
        return sorted(dorms)

    def all_dormitory_format(self):
        """二元组格式所有宿舍号"""
        dorms = []
        for dorm in self.all_dormitory():
            dorms.append((dorm, dorm))
        return tuple(dorms)

    def dormitory_by_manager(self, manager):
        """获取指定宿管员管理的宿舍"""
        # 管理员用户拥有所有宿舍权限
        if manager in self.manager:
            return self.all_dormitory()

        ar = self.dorm().get(manager)
        if ar is not None:
            # print(ar)
            return sorted(ar)
        else:
            return []

    def get_class(self, dor):
        """返回指定宿舍所属班级字符串"""
        # 取得班级字符串列表、年级
        cl = self.get_classes(dor)
        gd = cl[0][:2]

        # 班级数字列表
        csl = []
        for gc in cl:
            # print(gc)
            cs = self.num_regex.findall(gc)[0]
            csl.append(cs)

        # 班级数字字符串
        cs_str = '/'.join(csl)

        # 返回处理结果
        return gd + cs_str + '班'

    def get_classes(self, dor):
        """返回指定宿舍所属班级列表"""
        cl = []
        for ob in models.NewStudent.objects.filter(dorm=dor, graduated=False):
            # 记录学年班级
            ygc = ob.gc

            # 解析逻辑年级和班级数字
            lgd = ygc[:5]
            cs = int(ygc[5:7])

            # 合成班级字符串
            gd = self.logic_grade_reverse[lgd]
            gc = gd + str(cs) + '班'

            # 加入列表
            cl.append(gc)

        # 返回
        cl = list(set(cl))
        return cl

    def get_grade(self, _str):
        """根据班级字符串取得年级字符串"""
        for grade in self.grade:
            if grade[1] in _str:
                return grade[0]

    def get_grade_by_dorm(self, dor):
        """返回宿舍所属年级数字"""
        return self.get_grade(self.get_class(dor))

    def get_dormitory_by_grade(self, grade, gender=None):
        """取得某个年级所有宿舍(grade为数字)"""
        dorms = []
        for dorm in self.all_dormitory(gender=gender):
            try:
                if self.get_grade_by_dorm(dorm) == grade:
                    dorms.append(dorm)
            except IndexError:
                # 该宿舍没有学生入住，直接跳过即可
                pass
        return dorms

    def get_dormitory_by_grade1(self, grade, gender=None):
        """以一种更低复杂度的方式取得某个年级所有宿舍(grade为数字)"""
        # 根据年级数字取得逻辑年级字符串
        gd = self.grade_dict[grade]
        lgd = self.logic_grade[gd]

        # 获取年级所有学生对象
        if gender is None:
            students = models.NewStudent.objects.filter(grade_year_str=lgd, graduated=False)
        else:
            gender_ch = self.gender_ec[gender]
            students = models.NewStudent.objects.filter(grade_year_str=lgd, gender=gender_ch, graduated=False)

        # 初始化宿舍列表
        dorms = []

        # 加入宿舍
        for student in students:
            if student.dorm not in dorms:
                dorms.append(student.dorm)

        return dorms

    def get_dormitory_by_gc(self, gc, gender=None):
        """获取一个班学生所有可能的宿舍号（可分性别）"""
        dorms = []
        for dorm in self.all_dormitory(gender=gender):
            # print(dorm)
            if gc in self.get_classes(dorm):
                dorms.append(dorm)
        return dorms

    def get_cs(self, class_and_grade):
        """根据班级名称返回班级数字"""
        cs = int(self.num_regex.findall(class_and_grade)[0])
        return cs

    def get_manager(self, dorm):
        """取得该宿舍的管理员"""
        for manager in self.dorm().keys():
            if dorm in self.dorm()[manager]:
                return manager

    def get_date_group(self, date_time):
        """根据添加时间得出日期分组"""
        return datetime.datetime.date(date_time.astimezone(tz=self.tz))

    def get_gc(self):
        """生成所有班级并格式化输出"""
        gc_list = []
        for grade in self.grade:
            for i in range(12):
                gc = grade[1] + str(i + 1) + '班'
                gc_list.append((gc, gc))
        return tuple(gc_list)

    def get_grade_class(self):
        """取得年级与班级对应字典"""
        grade_class = {}
        for grade in self.grade:
            cl = []
            for i in range(12):
                gc = grade[1] + str(i + 1) + '班'
                cl.append(gc)
            grade_class[grade[1]] = cl
        return grade_class

    def get_class_dorm(self, gender=None):
        """取得班级与宿舍号对应字典"""
        class_dorm = {}
        for gc in self.get_gc():
            dl = self.get_dormitory_by_gc(gc[0], gender)
            class_dorm[gc[0]] = dl
        return class_dorm

    def get_class_dorm1(self, gender=None):
        """以一种更低复杂度的方式取得班级与宿舍号对应字典"""
        class_dorm = {}
        for gc_tup in self.get_gc():
            # 取得逻辑班级字符串
            gc = gc_tup[0]
            gd = gc[:2]
            lgd = self.logic_grade[gd]
            cs = gc[2:-1]
            if len(cs) == 1:
                cs = '0' + cs
            lgc = lgd + cs + '班'

            # 获取班级所有学生对象（可分性别）
            if gender is None:
                students = models.NewStudent.objects.filter(gc=lgc, graduated=False)
            else:
                gender_ch = self.gender_ec[gender]
                students = models.NewStudent.objects.filter(gc=lgc, gender=gender_ch, graduated=False)

            # 遍历所有学生对象，装入所有可能宿舍
            class_dorm[gc] = []
            for student in students:
                if student.dorm not in class_dorm[gc]:
                    class_dorm[gc].append(student.dorm)

        return class_dorm

    @staticmethod
    def get_date_group_str(dt):
        """根据日期分组得出其字符串表示"""
        dt_1 = dt + datetime.timedelta(days=1)
        dt_str = datetime.datetime.strftime(dt, '%Y-%m-%d')
        dt_1_str = datetime.datetime.strftime(dt_1, '%Y-%m-%d')
        return '{}中午——{}早上'.format(dt_str, dt_1_str)

    @staticmethod
    def date_group_from_str(dt_str):
        """上面函数的反函数"""
        dtm = datetime.datetime.strptime(dt_str[:10], '%Y-%m-%d')
        return datetime.datetime.date(dtm)

    @staticmethod
    def get_school_year():
        """获取当前学年，并格式化输出"""
        # 获取年月
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month

        # 生成学年字符串表示
        if month <= 8:
            start_year = year - 1
        else:
            start_year = year
        end_year = start_year + 1
        school_year_now = '{}~{}学年'.format(start_year, end_year)

        # 上一学年
        school_year_before = '{}~{}学年'.format(start_year - 1, end_year - 1)

        return (
            (school_year_now, school_year_now),
            (school_year_before, school_year_before),
        )

    @staticmethod
    def str_four(n):
        """整数n格式化为四位数字字符串"""
        if n < 10:
            return '000' + str(n)
        elif n < 100:
            return '00' + str(n)
        elif n < 1000:
            return '0' + str(n)
        else:
            return str(n)

    @staticmethod
    def str_two(n):
        """整数n格式化为两位数字字符串"""
        if n < 10:
            return '0' + str(n)
        else:
            return str(n)

    @staticmethod
    def get_students(gc):
        """以列表形式返回一个班级所有学生"""
        student_list = []
        for ob in models.NewStudent.objects.filter(gc=gc):
            student_list.append(ob.name)
        return sorted(student_list, key=lambda x: ''.join(lazy_pinyin(x)))

    def format_gc_students(self):
        """返回班级学生对应格式化字典"""
        # 初始化存放字典
        gs_dict = {}

        # 三个年级
        for grade in ['高一', '高二', '高三']:
            # 逻辑年级
            lg = self.logic_grade[grade]

            # 12个班
            for cs in range(1, 13):
                # 合成班级字符串
                cs_str = self.str_two(cs)
                gc = lg + cs_str + '班'

                # 加入字典
                gs_dict[gc] = self.get_students(gc)

        return gs_dict

    def get_logic_gc(self, gc):
        """
            原始班级字符串转换为逻辑班级字符串
            例：高一1班➡2024级01班
        """
        # 取得年级，转换为逻辑年级
        gd = gc[:2]
        lgd = self.logic_grade[gd]

        # 获取班级数字
        cs = int(gc[2:-1])

        # 两位化处理
        cs_str = self.str_two(cs)

        # 拼接成逻辑班级字符串
        lgc = lgd + cs_str + '班'
        return lgc

    def get_original_gc(self, lgc):
        """
            逻辑班级字符串转换为原始班级字符串
            例：2023级01班➡高二1班
        """
        # 取得逻辑年级，转为原始年级
        lgd = lgc[:5]
        gd = self.logic_grade_reverse[lgd]

        # 获取班级数字
        cs = int(lgc[5:7])

        # 拼接成原始班级字符串
        gc = gd + str(cs) + '班'
        return gc

    @staticmethod
    def get_old_new(grade=0, year=None):
        """取得原宿舍与新宿舍对应字典"""
        # 确保服务器上进入正确的目录，可正常运行
        if os.name != 'nt':
            os.chdir('/root/dormitory_manager/dm')

        # 根据当前年份合成json文件路径
        if year is None:
            year = datetime.datetime.now().year
        filepath = 'media/old_new_{}.json'.format(year)

        # 读取字典或列表
        with open(filepath) as f:
            if grade:
                old_new = json.loads(f.read())[grade - 1]
            else:
                old_new = json.loads(f.read())
        return old_new

    @staticmethod
    def compare_list_more(al, bl):
        """比较两个列表中各自多余的部分"""
        # 去重
        alc = list(set(al))
        blc = list(set(bl))

        # 创建副本
        amb, bma = alc[:], blc[:]

        # a列表副本删除在b列表的元素
        for a in alc:
            if a in blc:
                amb.remove(a)

        # b列表副本删除在a列表的元素
        for b in blc:
            if b in alc:
                bma.remove(b)

        # 输出
        return sorted(amb), sorted(bma)

    def compare_all_dorms(self):
        """比较用两种方法生成的所有宿舍多余元素"""
        return self.compare_list_more(self.all_dormitory(), self.get_all_dormitory())

    def refresh_browser(self):
        """刷新浏览器"""
        # 关闭可能已存在的浏览器
        try:
            self.b.quit()
        except AttributeError:
            pass

        # 打开新的浏览器
        if os.name == 'nt':
            driver_path = ChromeDriverManager().install()
        else:
            driver_path = '/root/dormitory_manager/test/chromedriver-linux64/chromedriver'

        # 浏览器配置
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        # 打开浏览器
        self.b = webdriver.Chrome(options=chrome_options, service=Service(driver_path))


# def test():
#     """做个测试"""
#     dt = Data()
#     with open('dorm_manager.json', 'w', encoding='gbk') as f:
#         f.write(json.dumps(dt.dorm, ensure_ascii=False))
#
#
# if __name__ == '__main__':
#     test()
