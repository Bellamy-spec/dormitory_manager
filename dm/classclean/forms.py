"""用来新增记录的表单"""
from django import forms
from .models import ClassCleanRecord, ClassCleanScore, OutLookRecord


class RecordForm(forms.ModelForm):
    class Meta:
        model = ClassCleanRecord
        fields = ['grade', 'cs', 'tm', 'area', 'decrease', 'reason']
        labels = {
            'grade': '年级',
            'cs': '班级',
            'tm': '时间段',
            'area': '问题区域',
            'decrease': '扣分分值',
            'reason': '具体情况',
        }
        widgets = {
            'grade': forms.Select(attrs={'id': 'grade', 'onchange': 'show_selection()'}),
            'cs': forms.Select(attrs={'id': 'cs', 'onchange': 'fill_area()'}),
            'area': forms.Select(attrs={'id': 'area', 'onchange': 'select_cs()'}),
        }


class ScoreForm(forms.ModelForm):
    class Meta:
        model = ClassCleanScore
        fields = ['owner', 'pwd', 'score']
        labels = {'score': '卫生得分', 'owner': '检查人代号', 'pwd': '检查码'}
        widgets = {
            'owner': forms.TextInput(attrs={'id': 'owner', 'type': 'number'}),
            'pwd': forms.TextInput(attrs={'type': 'password', 'id': 'pwd'}),
        }


class OutLookRecordForm(forms.ModelForm):
    class Meta:
        model = OutLookRecord
        fields = ['owner', 'pwd']
        labels = {'owner': '检查人代号', 'pwd': '检查码'}
        widgets = {
            'owner': forms.TextInput(attrs={'id': 'owner', 'type': 'number'}),
            'pwd': forms.TextInput(attrs={'type': 'password', 'id': 'pwd'}),
        }
