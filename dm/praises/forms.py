# coding=utf-8
"""表单文件"""
from django import forms
from .models import Task, ClassSubmit, StudentSubmit


class TaskForm(forms.ModelForm):
    """用于发布任务的表单"""
    class Meta:
        model = Task
        fields = ['term', 'cert_date']
        labels = {'term': '学期', 'cert_date': '证书日期'}
        widgets = {
            'cert_date': forms.TextInput(attrs={'type': 'date'}),
        }


class ClassSubmitForm(forms.ModelForm):
    """班级提交表单"""
    class Meta:
        model = ClassSubmit
        fields = ['gc', 'xlsx_file']
        labels = {'gc': '选择上报班级', 'xlsx_file': '上传获奖学生名单文件'}


class ChangeDateForm(forms.ModelForm):
    """用于修改证书日期的表单"""
    class Meta:
        model = Task
        fields = ['cert_date']
        labels = {'cert_date': '证书日期'}
        widgets = {
            'cert_date': forms.TextInput(attrs={'type': 'date'}),
        }


class TempAddForm(forms.Form):
    """用于二次模板批量上传的表单"""
    file = forms.FileField(label='上传获奖学生名单文件')


class AddStudentForm(forms.ModelForm):
    """用于单个添加获奖学生的表单"""
    class Meta:
        model = StudentSubmit
        fields = ['name', 'praise_name']
        labels = {'name': '学生姓名', 'praise_name': '奖项名称'}
        widgets = {
            'name': forms.Select(attrs={'id': 'nm'}),
            'praise_name': forms.Select(attrs={'id': 'praise_nm'}),
        }
