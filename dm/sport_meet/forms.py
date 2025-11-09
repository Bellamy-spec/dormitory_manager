"""表单"""
from django import forms
from .models import PutName


class PutNameForm(forms.ModelForm):
    """用于报名项目的表单"""
    class Meta:
        model = PutName
        fields = ['class_and_grade', 'name', 'gender', 'item']
        labels = {
            'class_and_grade': '班级',
            'name': '姓名',
            'gender': '性别',
            'item': '报名项目',
        }
        widgets = {
            'class_and_grade': forms.Select(attrs={'id': 'gc', 'onchange': 'load_name()'}),
            'name': forms.Select(attrs={'id': 'nm'}),
        }
