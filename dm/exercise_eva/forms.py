# coding=utf-8
"""课间操评价系统的表单文件"""
from django import forms
from .models import ShortAbst, ExerciseScore, ECOScore


class ShortAbstForm(forms.ModelForm):
    """用于登记短假学生的表单"""
    class Meta:
        model = ShortAbst
        fields = ['class_and_grade', 'name']
        labels = {
            'class_and_grade': '班级',
            'name': '姓名',
        }
        widgets = {
            'class_and_grade': forms.Select(attrs={'id': 'gc', 'onchange': 'load_students()'}),
            'name': forms.Select(attrs={'id': 'nm'}),
        }


class ExerciseScoreForm(forms.ModelForm):
    """用于上传每天课间操检查数据的表单"""
    class Meta:
        model = ExerciseScore
        fields = ['class_and_grade', 'act_come', 'late_come', 'no_wear', 'quality_score', 'owner', 'pwd']
        labels = {
            'class_and_grade': '班级',
            'act_come': '实际跑操人数',
            'late_come': '迟到人数',
            'no_wear': '未穿校服人数',
            'quality_score': '质量分',
            'owner': '检查人代号',
            'pwd': '检查人密码',
        }
        widgets = {
            'owner': forms.TextInput(attrs={'id': 'owner', 'type': 'number'}),
            'pwd': forms.TextInput(attrs={'id': 'pwd', 'type': 'password'}),
        }


class ECOScoreForm(forms.ModelForm):
    """用于登记节能检查情况的表单"""
    class Meta:
        model = ECOScore
        fields = ['class_and_grade', 'owner', 'pwd']
        labels = {
            'class_and_grade': '班级',
            'owner': '检查人代号',
            'pwd': '检查人密码',
        }
        widgets = {
            'owner': forms.TextInput(attrs={'id': 'owner', 'type': 'number'}),
            'pwd': forms.TextInput(attrs={'id': 'pwd', 'type': 'password'}),
        }
