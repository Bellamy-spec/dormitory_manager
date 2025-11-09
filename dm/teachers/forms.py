"""表单"""
from django import forms
from .models import Teacher


class TeacherForm(forms.ModelForm):
    """用来收集教师信息的表单"""
    class Meta:
        model = Teacher
        fields = ['name', 'gender', 'id_number']
        labels = {
            'name': '姓名',
            'gender': '性别',
            'id_number': '身份证号',
        }
