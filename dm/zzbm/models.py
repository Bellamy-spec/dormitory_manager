from django.db import models
import random
from datetime import datetime, date
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from .tools import DataTool


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class Task(models.Model):
    """任务类"""
    # TODO:表单填写字段
    # 任务截止日期
    end_date = models.DateField()

    # TODO:系统生成或更改字段
    # 任务年份
    year = models.CharField(max_length=4)

    # 任务活跃状态
    active = models.BooleanField(default=True)
    changed = models.BooleanField(default=False)

    # 已报名学生数
    added = models.IntegerField(default=0)

    # TODO:动态调整字段
    # 每个考场的考生数，若为零则不可分考场
    max_len = models.IntegerField(default=30)

    # 准考证号第8位为0时考试开始时间
    start_time = models.CharField(max_length=19, default='', blank=True)
    format_start_time = models.CharField(max_length=16, default='', blank=True)
    exam_time_active = models.BooleanField(default=False)
    full1 = models.BooleanField(default=False)
    full2 = models.BooleanField(default=False)
    start_time_ob = models.DateTimeField(blank=True, null=True)

    # 准考证号第8位为1时考试开始时间
    start_time_1 = models.CharField(max_length=19, default='', blank=True)
    format_start_time_1 = models.CharField(max_length=16, default='', blank=True)
    exam_time_active_1 = models.BooleanField(default=False)
    full1_1 = models.BooleanField(default=False)
    full2_1 = models.BooleanField(default=False)
    start_time_ob_1 = models.DateTimeField(blank=True, null=True)

    # 准考证号第8位为2时考试开始时间
    start_time_2 = models.CharField(max_length=19, default='', blank=True)
    format_start_time_2 = models.CharField(max_length=16, default='', blank=True)
    exam_time_active_2 = models.BooleanField(default=False)
    full1_2 = models.BooleanField(default=False)
    full2_2 = models.BooleanField(default=False)
    start_time_ob_2 = models.DateTimeField(blank=True, null=True)

    # 准考证号第8位为3时考试开始时间
    start_time_3 = models.CharField(max_length=19, default='', blank=True)
    format_start_time_3 = models.CharField(max_length=16, default='', blank=True)
    exam_time_active_3 = models.BooleanField(default=False)
    full1_3 = models.BooleanField(default=False)
    full2_3 = models.BooleanField(default=False)
    start_time_ob_3 = models.DateTimeField(blank=True, null=True)

    # 准考证号第8位为4时考试开始时间
    start_time_4 = models.CharField(max_length=19, default='', blank=True)
    format_start_time_4 = models.CharField(max_length=16, default='', blank=True)
    exam_time_active_4 = models.BooleanField(default=False)
    full1_4 = models.BooleanField(default=False)
    full2_4 = models.BooleanField(default=False)
    start_time_ob_4 = models.DateTimeField(blank=True, null=True)

    # 准考证号第8位为5时考试开始时间
    start_time_5 = models.CharField(max_length=19, default='', blank=True)
    format_start_time_5 = models.CharField(max_length=16, default='', blank=True)
    exam_time_active_5 = models.BooleanField(default=False)
    full1_5 = models.BooleanField(default=False)
    full2_5 = models.BooleanField(default=False)
    start_time_ob_5 = models.DateTimeField(blank=True, null=True)

    # 准考证是否可下载
    open_download = models.BooleanField(default=False)

    # 考场总数
    max_room = models.IntegerField(default=0)

    # 各场次最大已分配考场、人数；分科：其中1为素描或创意画，2为书法或国画
    mr1 = models.IntegerField(default=0)
    mr2 = models.IntegerField(default=50)
    total1 = models.IntegerField(default=0)
    total2 = models.IntegerField(default=0)
    mr_show = models.CharField(max_length=50, default='', blank=True)
    total_show = models.CharField(max_length=50, default='', blank=True)

    mr1_1 = models.IntegerField(default=0)
    mr2_1 = models.IntegerField(default=50)
    total1_1 = models.IntegerField(default=0)
    total2_1 = models.IntegerField(default=0)
    mr_show_1 = models.CharField(max_length=50, default='', blank=True)
    total_show_1 = models.CharField(max_length=50, default='', blank=True)

    mr1_2 = models.IntegerField(default=0)
    mr2_2 = models.IntegerField(default=50)
    total1_2 = models.IntegerField(default=0)
    total2_2 = models.IntegerField(default=0)
    mr_show_2 = models.CharField(max_length=50, default='', blank=True)
    total_show_2 = models.CharField(max_length=50, default='', blank=True)

    mr1_3 = models.IntegerField(default=0)
    mr2_3 = models.IntegerField(default=50)
    total1_3 = models.IntegerField(default=0)
    total2_3 = models.IntegerField(default=0)
    mr_show_3 = models.CharField(max_length=50, default='', blank=True)
    total_show_3 = models.CharField(max_length=50, default='', blank=True)

    mr1_4 = models.IntegerField(default=0)
    mr2_4 = models.IntegerField(default=50)
    total1_4 = models.IntegerField(default=0)
    total2_4 = models.IntegerField(default=0)
    mr_show_4 = models.CharField(max_length=50, default='', blank=True)
    total_show_4 = models.CharField(max_length=50, default='', blank=True)

    mr1_5 = models.IntegerField(default=0)
    mr2_5 = models.IntegerField(default=50)
    total1_5 = models.IntegerField(default=0)
    total2_5 = models.IntegerField(default=0)
    mr_show_5 = models.CharField(max_length=50, default='', blank=True)
    total_show_5 = models.CharField(max_length=50, default='', blank=True)

    # 分配完一轮
    turn1 = models.IntegerField(default=0)
    turn2 = models.IntegerField(default=0)

    # 准考证号第8位起始数字
    start_turn = models.IntegerField(default=0)

    # 报名自动分配考场
    auto_give = models.BooleanField(default=False)

    # 是否可查成绩
    can_que = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{}中招美术测试试报名'.format(self.year)

    def give_year(self):
        """生成年份"""
        year = datetime.now().year
        self.year = str(year)

    def update_active(self):
        """过期自动截止"""
        if not self.changed and date.today() > self.end_date:
            self.active = False
            self.changed = True
            self.save()

    def judge_type(self, rm):
        """判断rm考场类型"""
        try:
            # 返回找到的第一个考生的科目类别
            return Student.objects.filter(task_belong=self, room=rm)[0].subject
        except IndexError:
            # 未找到，返回空值
            return None

    def get_room_dict(self):
        """返回各考场人数字典"""
        room_dict = {}

        # 循环遍历所有考生，记录各考场人数
        for student in Student.objects.filter(task_belong=self, add_method=1).order_by('room'):
            if student.room != '未分配':
                room_dict.setdefault(student.room, int(student.seat))

                # 保证值是该考场最大考号
                if int(student.seat) > room_dict[student.room]:
                    room_dict[student.room] = int(student.seat)

        return room_dict

    def all_room(self, e8):
        """返回所有考场号（可选参数：考场号首位）"""
        room_list = []
        for student in Student.objects.filter(task_belong=self, add_method=1, num8=e8):
            room_list.append(student.room)

        room_list = list(set(room_list))
        room_list.sort()
        return room_list

    def get_mr(self, e8):
        """返回首位特定考场号的最大已分配考场"""
        mr1, mr2 = 0, 50
        for room in self.all_room(e8):
            ri = int(room[1:])
            if ri < 50:
                if mr1 < ri:
                    mr1 = ri
            else:
                if mr2 < ri:
                    mr2 = ri
        return mr1, mr2

    def make_show(self, num8):
        """生成已报名信息提示"""
        if num8 == '0':
            self.mr_show = '素描或创意画：{}，书法或国画：{}'.format(self.mr1, self.mr2)
            self.total_show = '素描或创意画：{}，书法或国画：{}'.format(self.total1, self.total2)
        elif num8 == '1':
            self.mr_show_1 = '素描或创意画：{}，书法或国画：{}'.format(self.mr1_1, self.mr2_1)
            self.total_show_1 = '素描或创意画：{}，书法或国画：{}'.format(self.total1_1, self.total2_1)
        elif num8 == '2':
            self.mr_show_2 = '素描或创意画：{}，书法或国画：{}'.format(self.mr1_2, self.mr2_2)
            self.total_show_2 = '素描或创意画：{}，书法或国画：{}'.format(self.total1_2, self.total2_2)
        elif num8 == '3':
            self.mr_show_3 = '素描或创意画：{}，书法或国画：{}'.format(self.mr1_3, self.mr2_3)
            self.total_show_3 = '素描或创意画：{}，书法或国画：{}'.format(self.total1_3, self.total2_3)
        elif num8 == '4':
            self.mr_show_4 = '素描或创意画：{}，书法或国画：{}'.format(self.mr1_4, self.mr2_4)
            self.total_show_4 = '素描或创意画：{}，书法或国画：{}'.format(self.total1_4, self.total2_4)
        elif num8 == '5':
            self.mr_show_5 = '素描或创意画：{}，书法或国画：{}'.format(self.mr1_5, self.mr2_5)
            self.total_show_5 = '素描或创意画：{}，书法或国画：{}'.format(self.total1_5, self.total2_5)

    def increase_room(self, subject, num8):
        """增加相应的考场数"""
        if subject == '素描或创意画':
            if num8 == '0':
                self.mr1 += 1
            elif num8 == '1':
                self.mr1_1 += 1
            elif num8 == '2':
                self.mr1_2 += 1
            elif num8 == '3':
                self.mr1_3 += 1
            elif num8 == '4':
                self.mr1_4 += 1
            elif num8 == '5':
                self.mr1_5 += 1
        elif subject == '书法或国画':
            if num8 == '0':
                self.mr2 += 1
            elif num8 == '1':
                self.mr2_1 += 1
            elif num8 == '2':
                self.mr2_2 += 1
            elif num8 == '3':
                self.mr2_3 += 1
            elif num8 == '4':
                self.mr2_4 += 1
            elif num8 == '5':
                self.mr2_5 += 1
        self.max_room += 1

    def decrease_room(self, subject, num8):
        """减少相应的考场数"""
        if subject == '素描或创意画':
            if num8 == '0':
                self.mr1 -= 1
            elif num8 == '1':
                self.mr1_1 -= 1
            elif num8 == '2':
                self.mr1_2 -= 1
            elif num8 == '3':
                self.mr1_3 -= 1
            elif num8 == '4':
                self.mr1_4 -= 1
            elif num8 == '5':
                self.mr1_5 -= 1
        elif subject == '书法或国画':
            if num8 == '0':
                self.mr2 -= 1
            elif num8 == '1':
                self.mr2_1 -= 1
            elif num8 == '2':
                self.mr2_2 -= 1
            elif num8 == '3':
                self.mr2_3 -= 1
            elif num8 == '4':
                self.mr2_4 -= 1
            elif num8 == '5':
                self.mr2_5 -= 1
        self.max_room -= 1

    def increase_student(self, subject, num8):
        """已分配考场的考生总数增加"""
        if subject == '素描或创意画':
            if num8 == '0':
                self.total1 += 1
            elif num8 == '1':
                self.total1_1 += 1
            elif num8 == '2':
                self.total1_2 += 1
            elif num8 == '3':
                self.total1_3 += 1
            elif num8 == '4':
                self.total1_4 += 1
            elif num8 == '5':
                self.total1_5 += 1
        elif subject == '书法或国画':
            if num8 == '0':
                self.total2 += 1
            elif num8 == '1':
                self.total2_1 += 1
            elif num8 == '2':
                self.total2_2 += 1
            elif num8 == '3':
                self.total2_3 += 1
            elif num8 == '4':
                self.total2_4 += 1
            elif num8 == '5':
                self.total2_5 += 1

    def decrease_student(self, subject, num8):
        """已分配考场的考生总数减少"""
        if subject == '素描或创意画':
            if num8 == '0':
                self.total1 -= 1
            elif num8 == '1':
                self.total1_1 -= 1
            elif num8 == '2':
                self.total1_2 -= 1
            elif num8 == '3':
                self.total1_3 -= 1
            elif num8 == '4':
                self.total1_4 -= 1
            elif num8 == '5':
                self.total1_5 -= 1
        elif subject == '书法或国画':
            if num8 == '0':
                self.total2 -= 1
            elif num8 == '1':
                self.total2_1 -= 1
            elif num8 == '2':
                self.total2_2 -= 1
            elif num8 == '3':
                self.total2_3 -= 1
            elif num8 == '4':
                self.total2_4 -= 1
            elif num8 == '5':
                self.total2_5 -= 1

    def set_full(self, subject, num8, total_max):
        """设置某科目某场次已满"""
        # print('\n\n\n')
        # print(self.total1)
        # print('\n\n\n')
        if subject == '素描或创意画':
            if num8 == '0':
                if self.total1 >= total_max:
                    self.full1 = True
            elif num8 == '1':
                if self.total1_1 >= total_max:
                    self.full1_1 = True
            elif num8 == '2':
                if self.total1_2 >= total_max:
                    self.full1_2 = True
            elif num8 == '3':
                if self.total1_3 >= total_max:
                    self.full1_3 = True
            elif num8 == '4':
                if self.total1_4 >= total_max:
                    self.full1_4 = True
            elif num8 == '5':
                if self.total1_5 >= total_max:
                    self.full1_5 = True
        elif subject == '书法或国画':
            if num8 == '0':
                if self.total2 >= total_max:
                    self.full2 = True
            elif num8 == '1':
                if self.total2_1 >= total_max:
                    self.full2_1 = True
            elif num8 == '2':
                if self.total2_2 >= total_max:
                    self.full2_2 = True
            elif num8 == '3':
                if self.total2_3 >= total_max:
                    self.full2_3 = True
            elif num8 == '4':
                if self.total2_4 >= total_max:
                    self.full2_4 = True
            elif num8 == '5':
                if self.total2_5 >= total_max:
                    self.full2_5 = True

        # 同场次两场均满则关闭报名
        if self.full1 and self.full2:
            self.exam_time_active = False
        if self.full1_1 and self.full2_1:
            self.exam_time_active_1 = False
        if self.full1_2 and self.full2_2:
            self.exam_time_active_2 = False
        if self.full1_3 and self.full2_3:
            self.exam_time_active_3 = False
        if self.full1_4 and self.full2_4:
            self.exam_time_active_4 = False
        if self.full1_5 and self.full2_5:
            self.exam_time_active_5 = False

        # 保存
        self.save()


class Student(models.Model):
    """考生类"""
    # TODO:以下字段考生通过表单填写
    # 姓名
    name = models.CharField(max_length=20)

    # 证件类型
    card_type = models.IntegerField(choices=((1, '居民二代身份证'),))

    # 证件号码
    id_number = models.CharField(max_length=18)

    # 手机号
    phone_number = models.CharField(max_length=11)

    # 邮箱
    email = models.CharField(max_length=25, blank=True)

    # 性别
    gender = models.CharField(max_length=1, choices=(('男', '男'), ('女', '女')))

    # 初中毕业学校
    middle_school = models.CharField(max_length=30, choices=DT.get_middle_school_choices())

    # 初中学校备注
    middle_school_desc = models.CharField(max_length=20, default='', blank=True)

    # 选考科目
    subject = models.CharField(max_length=6, choices=DT.subjects)

    # TODO:特殊方式处理，考试时间——准考证号第八位
    num8 = models.CharField(max_length=1, default='0', choices=DT.get_exam_time())

    # 照片
    photo = ProcessedImageField(upload_to='zzbm/', null=True, blank=True,
                                processors=[ResizeToFill(295, 413)],
                                format='JPEG',
                                options={'quality': 60}, verbose_name='一寸照片')

    # TODO:以下字段为系统生成
    # 分考场时生成：考场（三位）、座号（两位）、准考证号
    room = models.CharField(max_length=3, default='未分配')
    seat = models.CharField(max_length=3, default='未分配')
    exam_id = models.CharField(max_length=12, default='未分配')

    # 报名时生成：报名序号（口令）、报名序数
    pwd = models.CharField(max_length=6, default='000000')
    num = models.IntegerField()

    # 所属任务年份
    task_belong = models.ForeignKey(Task, on_delete=models.CASCADE)

    # 报名时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    # 考试成绩
    score = models.CharField(max_length=1, choices=tuple(DT.scores_2025.items()), default='O')

    # 添加方式
    add_method = models.IntegerField(choices=DT.add_method, default=1)

    # 是否缺考
    miss = models.BooleanField(default=False)

    # 是否需要提示
    mention = models.BooleanField(default=False)

    # 白名单：确认不需要提示
    white_name = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{}{}'.format(self.id_number, self.name)

    def update_pwd(self):
        """更新报名序号"""
        new_pwd = ''
        for i in range(6):
            new_pwd += str(random.randint(0, 9))
        self.pwd = new_pwd

    def make_exam_id(self):
        """根据考场和座号生成准考证号"""
        self.exam_id = '{}{}{}{}'.format(self.task_belong.year, DT.ei_mid, self.room, self.seat)

    def get_exam_time(self):
        """根据准考证号第8位确定考试时间"""
        e8 = self.room[0]
        if e8 == '0':
            return self.task_belong.start_time, self.task_belong.format_start_time
        elif e8 == '1':
            return self.task_belong.start_time_1, self.task_belong.format_start_time_1
        elif e8 == '2':
            return self.task_belong.start_time_2, self.task_belong.format_start_time_2
        elif e8 == '3':
            return self.task_belong.start_time_3, self.task_belong.format_start_time_3
        elif e8 == '4':
            return self.task_belong.start_time_4, self.task_belong.format_start_time_4
        elif e8 == '5':
            return self.task_belong.start_time_5, self.task_belong.format_start_time_5
