"""班会检查系统的表单文件"""
from django import forms
from .models import CMScore


class CMScoreForm(forms.ModelForm):
    class Meta:
        model = CMScore
        fields = ['owner', 'pwd', 'head_in', 'have_ppt', 'have_host', 'topic', 'decrease', 'score']
        labels = {
            'owner': '检查人代号',
            'pwd': '检查码',
            'head_in': '班主任是否在班',
            'have_ppt': '是否有课件',
            'have_host': '是否有主持人',
            'topic': '班会主题',
            'decrease': '纪律扣分',
            'score': '班会总体评价得分',
        }
        widgets = {
            'owner': forms.TextInput(attrs={'id': 'owner', 'type': 'number'}),
            'pwd': forms.TextInput(attrs={'type': 'password', 'id': 'pwd'}),
        }
