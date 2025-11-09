"""表单"""
from django import forms
from .models import Record, Investigation, Paper, NewStudent
from .data import Data


# 实例化静态数据类
DT = Data()


class RecordForm(forms.ModelForm):
    """用于新增记录的表单"""
    class Meta:
        model = Record
        fields = ['bed', 'tm', 'tp', 'reason']
        labels = {
            'bed': '床铺',
            'tm': '时间类型',
            'tp': '问题类型',
            'reason': '具体情况',
        }
        widgets = {
            'bed': forms.Select(attrs={'id': 'bed'}),
        }


class InvestigationForm(forms.ModelForm):
    """用于发布满意度调查的表单"""
    class Meta:
        model = Investigation
        fields = ['school_year']
        labels = {'school_year': '学年'}


class PaperForm(forms.ModelForm):
    """问卷填写表单"""
    class Meta:
        model = Paper
        fields = list(DT.paper_t.keys())
        labels = DT.paper_t
        widgets = {
            'gender': forms.Select(attrs={'id': 'gender', 'onchange': 'update_dorm()'}),
            'grade': forms.Select(attrs={'id': 'grade', 'onchange': 'update_cs()'}),
            'gc': forms.Select(attrs={'id': 'gc', 'onchange': 'update_dorm()'}),
            'dorm': forms.Select(attrs={'id': 'dorm'}),

            # 单选题设置
            't1': forms.RadioSelect(),
            't2': forms.RadioSelect(),
            't3': forms.RadioSelect(),
            't4': forms.RadioSelect(),
            't5': forms.RadioSelect(),
            't6': forms.RadioSelect(),
            't7': forms.RadioSelect(),
            't8': forms.RadioSelect(),
            't9': forms.RadioSelect(),
            't10': forms.RadioSelect(),
            't11': forms.RadioSelect(),
            't12': forms.RadioSelect(),
        }


class FileUploadForm(forms.Form):
    """文件加入新生表单"""
    file = forms.FileField(label='模板批量加入新生')


class SepChangeDormForm(forms.Form):
    """文件搬宿舍表单"""
    file = forms.FileField(label='模板批量搬宿舍')


class ChangeInfoForm(forms.ModelForm):
    """用于修改新生信息的表单"""
    class Meta:
        model = NewStudent
        fields = ['name', 'id_number', 'gender', 'cs', 'dorm', 'bed']
        labels = {
            'name': '姓名',
            'id_number': '身份证号',
            'gender': '性别',
            'cs': '班级',
            'dorm': '宿舍',
            'bed': '床铺号',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
        }


class AddLineForm(forms.Form):
    """用于新增宿舍搬迁轨迹的表单"""
    grade_index = forms.ChoiceField(
        choices=((0, '高一转新高二'), (1, '高二转新高三')),
        label='选择年级',
        widget=forms.Select(),
    )
    old_dorm = forms.CharField(max_length=3, min_length=3, label='原宿舍')
    new_dorm = forms.CharField(max_length=3, min_length=3, label='新宿舍')
