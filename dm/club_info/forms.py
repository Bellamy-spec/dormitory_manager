"""表单"""
from django import forms
from .models import Club, Member


class ClubForm(forms.ModelForm):
    """用于新建社团的表单"""
    class Meta:
        model = Club
        fields = ['name', 'desc']
        labels = {'name': '社团名称', 'desc': '社团简介'}
        widgets = {'desc': forms.Textarea()}


class MemberForm(forms.ModelForm):
    """用于录入成员的表单"""
    class Meta:
        model = Member
        fields = ['club_belong', 'name', 'id_number', 'tp']
        labels = {
            'club_belong': '所属社团',
            'name': '姓名',
            'id_number': '身份证号',
            'tp': '角色',
        }
