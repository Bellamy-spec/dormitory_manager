"""表单文件"""
from django import forms
from .models import Program, Performer, Costume, Designer


class ProgramForm(forms.ModelForm):
    """用于报名节目表演的表单"""
    class Meta:
        model = Program
        fields = ['name', 'tp', 'owner', 'owner_class', 'owner_phone', 'mac_nums',
                  'desc', 'etc']
        labels = {
            'name': '节目名称',
            'tp': '表演形式',
            'owner': '节目负责人姓名',
            'owner_class': '节目负责人所在班级',
            'owner_phone': '节目负责人联系方式',
            'mac_nums': '需要话筒数量',
            'desc': '节目简介',
            'etc': '备注',
        }
        widgets = {
            'owner_phone': forms.TextInput(attrs={'type': 'number'}),
            'desc': forms.Textarea(attrs={'placeholder': '请对节目做一个简单的介绍......'}),
            'etc': forms.Textarea(attrs={
                'placeholder': '请简要说明一下节目需要用到的道具、音乐、背景视频等'}),
        }


class CostumeForm(forms.ModelForm):
    """用于报名服装设计的表单"""
    class Meta:
        model = Costume
        fields = ['name', 'mt', 'mt_class', 'owner', 'owner_class',
                  'owner_phone', 'desc', 'drawing']
        labels = {
            'name': '服装名称',
            'mt': '服装模特',
            'mt_class': '模特所属班级（或教师）',
            'owner': '服装联络人',
            'owner_class': '联络人所在班级',
            'owner_phone': '联络人联系方式',
            'desc': '服装简介',
            'drawing': '服装设计图纸',
        }
        widgets = {
            'owner_phone': forms.TextInput(attrs={'type': 'number'}),
            'desc': forms.Textarea(attrs={'placeholder': '请简单介绍一下服装的设计理念......'}),
        }


class PerformerForm(forms.ModelForm):
    """用于新增节目表演者的表单"""
    class Meta:
        model = Performer
        fields = ['name', 'class_belong']
        labels = {'name': '表演者姓名', 'class_belong': '表演者所在班级（或教师）'}


class DesignerForm(forms.ModelForm):
    """用于新增服装设计师的表单"""
    class Meta:
        model = Designer
        fields = ['name', 'class_belong']
        labels = {'name': '设计师姓名', 'class_belong': '设计师所在班级'}


class SetNumForm(forms.ModelForm):
    """用于设置服装编号的表单"""
    class Meta:
        model = Costume
        fields = ['num']
        labels = {'num': ''}
