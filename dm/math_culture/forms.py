"""表单文件"""
from django import forms
from .models import Material


class ShareForm(forms.ModelForm):
    """用于上传素材的表单"""
    class Meta:
        model = Material
        fields = ['title', 'line', 'desc', 'file']
        labels = {
            'title': '标题',
            'line': '主线',
            'desc': '简介',
            'file': '上传附件',
        }
