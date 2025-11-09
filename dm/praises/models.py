# coding=utf-8
from django.db import models
from .tools import DataTool
import json
from dm.scores.models import get_students
import os
from PIL import Image, ImageDraw, ImageFont
import datetime


# 实例化静态数据类
DT = DataTool()


# Create your models here.
class Task(models.Model):
    """任务模型"""
    # 所属学期，格式例如2024-2025_2
    term = models.CharField(max_length=11, choices=DT.make_term_choices())

    # 证书日期
    cert_date = models.DateField(default=datetime.date.today())

    # 标题，格式例如2024~2025学年第2学期期末评优评先上报
    title = models.CharField(max_length=23)

    # 活跃状态（是否可上报）
    active = models.BooleanField(default=True)

    # 设置奖项及人数（系统根据用户前端输入合成）
    items_max = models.TextField()

    # 添加时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.title

    def make_title(self):
        """生成标题"""
        start_year = self.term[:4]
        end_year = self.term[5:9]
        term_idx = self.term[10]
        self.title = '{}~{}学年第{}学期期末评优评先上报'.format(start_year, end_year, term_idx)

    def get_items_max(self):
        """items_max字段解析为字典"""
        return json.loads(self.items_max)

    def load_items_max(self, imd):
        """字典保存为items_max字段"""
        self.items_max = json.dumps(imd)


class ClassSubmit(models.Model):
    """班级提交模型"""
    # 年级班级
    gc = models.CharField(max_length=5, choices=DT.make_gc_choices())
    grade_num = models.IntegerField()
    grade = models.CharField(max_length=2)
    cs = models.CharField(max_length=2)
    cs_int = models.IntegerField()

    # 所属任务
    task_belong = models.ForeignKey(Task, on_delete=models.CASCADE)

    # 获奖人名单excel表格文件
    xlsx_file = models.FileField(upload_to='praises/class_submit/')

    # 班级人数及学生名单（系统拉取）
    total = models.IntegerField()
    student_list = models.TextField()

    # 添加时间
    datetime_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.task_belong, self.gc)

    def fill_grade_cs(self):
        """根据班级字符串补全年级和班级数字信息"""
        self.grade = self.gc[:2]
        self.grade_num = DT.grades[self.grade]
        cs = self.gc[2:-1]
        self.cs_int = int(cs)
        if len(cs) < 2:
            cs = '0' + cs
        self.cs = cs

    def fill_students(self):
        """获取班级人数和学生名单"""
        student_list = get_students(self.gc, logic=False)
        self.student_list = json.dumps(student_list)
        self.total = len(student_list)

    def get_student_list(self):
        """获取学生列表"""
        return json.loads(self.student_list)

    def get_items_max(self):
        """获取奖项-最大人数字典"""
        imd = {}
        for item, max_tup in self.task_belong.get_items_max().items():
            if max_tup[0]:
                # 最大人数限制为比例，计算实际人数
                max_n = round(self.total * max_tup[1])
            else:
                # 最大人数限制直接为人数
                max_n = max_tup[1]
            imd[item] = max_n
        return imd

    def get_praise_students(self):
        """获取奖项-学生字典"""
        # 获取奖项
        praise_key = self.task_belong.get_items_max().keys()

        # 生成字典
        praise_students = {}
        for praise_name in praise_key:
            praise_students.setdefault(praise_name, [])
            for student in StudentSubmit.objects.filter(class_belong=self, praise_name=praise_name):
                praise_students[praise_name].append(student.name)
        return praise_students

    def get_max_num(self):
        """获取最大班内学号"""
        max_num = 0
        for student_submit in StudentSubmit.objects.filter(class_belong=self):
            if max_num < student_submit.num:
                max_num = student_submit.num
        return max_num


class StudentSubmit(models.Model):
    """学生提交模型"""
    # 学生姓名
    name = models.CharField(max_length=5)

    # 所属班级
    class_belong = models.ForeignKey(ClassSubmit, on_delete=models.CASCADE)

    # 奖项名称
    praise_name = models.CharField(max_length=10)

    # 班内编号
    num = models.IntegerField(default=0)

    # 证书模板
    cert = models.ImageField(upload_to='praises/cert/')
    cert_simple = models.ImageField(upload_to='praises/cert_simple/')

    def __str__(self):
        """返回模型的字符串表示"""
        return '{} {}'.format(self.class_belong, self.name)

    def get_num(self):
        """获取班内编号"""
        self.num = self.class_belong.get_max_num() + 1

    def make_cert(self, simple=True):
        """生成并保存获奖证书"""
        # 确保服务器上进入正确的目录，可正常运行
        if os.name != 'nt':
            os.chdir('/root/dormitory_manager/dm')

        # 获取所属班级及任务对象
        class_submit = self.class_belong
        task = class_submit.task_belong

        # 确定保存路径
        if simple:
            save_path = os.path.join(DT.base_dir, 'media', 'praises', 'cert_simple')
        else:
            save_path = os.path.join(DT.base_dir, 'media', 'praises', 'cert')
        save_path = os.path.join(save_path, '{}_{}_{}_{}.png'.format(
            task.term, class_submit.grade_num, class_submit.cs, self.num))

        # 获取四段文字内容
        call_text = DT.call_text.format(self.name)
        text_text = DT.text_text.format(task.title[:-8], self.praise_name)
        down_text = DT.down_text
        date_text = DT.date_text.format(task.cert_date.year, task.cert_date.month, task.cert_date.day)

        # 设置字体
        text_font = ImageFont.truetype('font/simsun.ttc', 54)

        # 打开新的图象
        image = Image.new('RGBA', (DT.cert_width, DT.cert_height), (255, 255, 255))
        draw = ImageDraw.Draw(image)

        # 添加背景
        if not simple:
            bg = Image.open(os.path.join('media', 'praises', 'cert_bg.png'))
            # print(bg.size)
            bg = bg.resize((DT.cert_width, DT.cert_height))
            # print(bg.size)
            image.paste(bg, (0, 0))

        # 添加称呼
        draw.text((250, 470), call_text, font=text_font, fill='black')

        # 计算自动换行宽度
        wrap_width = DT.cert_width - 500

        # 正文换行
        text_list = []
        line = ''
        written_width = 0
        for char in text_text:
            # 计算单个字符所占宽度
            char_width = draw.textsize(char, font=text_font)[0]

            # 判断添加此字符后是否超出宽度
            if written_width + char_width <= wrap_width:
                # 未超出，加入本行
                line += char
                written_width += char_width
            else:
                # 本行已满，开辟新行
                text_list.append(line)
                line = char
                written_width = char_width

        # 末行加入
        text_list.append(line)

        # 添加换行后的正文
        h = 570
        for text_line in text_list:
            draw.text((250, h), text_line, font=text_font, fill='black')
            h += 100

        # 添加落款（右对齐）
        down_width = draw.textsize(down_text, font=text_font)[0]
        down_x = DT.cert_width - 275 - down_width
        draw.text((down_x, 820), down_text, font=text_font, fill='black')

        # 添加日期（右对齐）
        date_width = draw.textsize(date_text, font=text_font)[0]
        date_x = DT.cert_width - 275 - date_width
        draw.text((date_x, 920), date_text, font=text_font, fill='black')

        # 盖章
        if not simple:
            zhang = Image.open(os.path.join('media', 'praises', 'zhang_dy.png'))
            zhang = zhang.resize((int(zhang.width * 0.6), int(zhang.height * 0.6)))
            image.paste(zhang, (1100, 750), mask=zhang)

        # 保存
        image.save(save_path)

        # 设置属性
        if simple:
            self.cert_simple = save_path
        else:
            self.cert = save_path


# def test():
#     """做个测试"""
#     from praises.models import StudentSubmit
#     StudentSubmit.objects.all()[0].make_cert(simple=False)
#
#
# if __name__ == '__main__':
#     test()
