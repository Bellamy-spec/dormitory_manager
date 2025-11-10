"""表单"""
from django import forms
from .models import Class, Student


class ClassForm(forms.ModelForm):
    """用于编辑班级情况的表单"""
    class Meta:
        model = Class
        fields = ['total']
        labels = {'total': '应到人数'}


class StudentForm(forms.ModelForm):
    """用于新增请假学生的表单"""
    class Meta:
        model = Student
        fields = ['name', 'gender', 'dorm', 'reason']
        labels = {
            'name': '姓名',
            'gender': '性别',
            'dorm': '宿舍',
            'reason': '请假原因及预计返校时间',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off', 'list': 'st-list'}),
            'reason': forms.Textarea(),
        }
