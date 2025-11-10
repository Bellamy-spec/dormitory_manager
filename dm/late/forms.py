"""迟到记录程序的表单"""
from django import forms
from .models import LateStudent


class StudentForm(forms.ModelForm):
    """新增迟到学生的表单"""
    class Meta:
        model = LateStudent
        fields = ['name', 'tm']
        labels = {'name': '姓名', 'tm': '迟到时间'}
