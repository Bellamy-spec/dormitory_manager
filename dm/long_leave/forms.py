"""表单"""
from django import forms
from .models import LongLeaveRecord, ClassInfo, AbsentStudents
from datetime import date


class LongLeaveForm(forms.ModelForm):
    """用于新增人员的表单"""
    class Meta:
        model = LongLeaveRecord
        fields = ['name', 'class_and_grade', 'end_date', 'tp', 'desc']
        labels = {
            'name': '姓名',
            'class_and_grade': '班级',
            'end_date': '截止日期',
            'tp': '是否留在教室',
            'desc': '备注',
        }
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.Select(attrs={'id': 'name', 'onchange': 'config_gc()'}),
            'class_and_grade': forms.Select(attrs={'id': 'gc', 'onchange': 'reload_students()'}),
        }


class ClassForm(forms.ModelForm):
    """用于上报每日班级人员信息的表单"""
    class Meta:
        model = ClassInfo
        fields = ['date', 'grade', 'cs', 'total']
        labels = {'date': '日期', 'grade': '年级', 'cs': '班级', 'total': '应到人数'}
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'value': date.today()}),
            'grade': forms.Select(attrs={'id': 'grade', 'onchange': 'show_selection()'}),
            'cs': forms.Select(attrs={'id': 'cs'}),
            'total': forms.TextInput(attrs={'id': 'total', 'type': 'number'}),
        }


class ChangeTotalForm(forms.ModelForm):
    """用于更改已提交班级应到人数的表单"""
    class Meta:
        model = ClassInfo
        fields = ['total']
        labels = {'total': ''}


class AddAbsentForm(forms.ModelForm):
    """用于已提交班级新增请假学生的表单"""
    class Meta:
        model = AbsentStudents
        fields = ['name', 'reason']
        labels = {'name': '学生姓名', 'reason': '请假原因'}
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off', 'list': 'st-list'}),
        }
