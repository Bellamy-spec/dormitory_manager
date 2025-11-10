"""中招美术加试报名系统的表单文件"""
from django import forms
from .models import Task, Student
from datetime import date


class TaskForm(forms.ModelForm):
    """用于发布任务的表单"""

    class Meta:
        model = Task
        fields = ['end_date']
        labels = {'end_date': '设置截止日期'}
        widgets = {
            'end_date': forms.TextInput(attrs={
                'type': 'date',
                'min': date.today().strftime('%Y-%m-%d'),
                'max': '{}-12-31'.format(date.today().year),
            }),
        }


class PutNameForm(forms.ModelForm):
    """用于考生报名的表单"""

    class Meta:
        model = Student
        fields = [
            'name',
            'gender',
            'card_type',
            'id_number',
            'phone_number',
            # 'email',
            'middle_school',
            'subject',
            'photo',
        ]
        labels = {
            'name': '姓名',
            'gender': '性别',
            'card_type': '证件类型',
            'id_number': '证件号码',
            'phone_number': '手机号',
            # 'email': '邮箱(选填，可用于找回报名序号)',
            'middle_school': '初中毕业学校',
            'subject': '选考科目',
            'photo': '上传个人一寸照片',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'type': 'number'}),
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'middle_school': forms.TextInput(attrs={'autocomplete': 'off'}),
            'id_number': forms.TextInput(attrs={'autocomplete': 'off'}),
        }


class FileUploadForm(forms.Form):
    """文件上传成绩表单"""
    file = forms.FileField(label='模板上传成绩')


class StudentsUploadForm(forms.Form):
    """文件批量导入考生表单"""
    file = forms.FileField(label='模板批量导入考生')


class ChangeInfoForm(forms.ModelForm):
    """用于修改导入考生信息的表单"""

    class Meta:
        model = Student
        fields = ['name', 'gender', 'id_number', 'phone_number', 'middle_school', 'subject']
        labels = {
            'name': '姓名',
            'gender': '性别',
            'id_number': '身份证号',
            'phone_number': '手机号',
            'middle_school': '初中毕业学校',
            'subject': '选考科目',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'type': 'number'}),
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'middle_school': forms.TextInput(attrs={'autocomplete': 'off'}),
            'id_number': forms.TextInput(attrs={'autocomplete': 'off'}),
        }


class ChangePutForm(forms.ModelForm):
    """用于修改考生信息的表单"""

    class Meta:
        model = Student
        fields = [
            'name',
            'gender',
            'card_type',
            'id_number',
            'phone_number',
            'middle_school',
            'subject',
            'photo',
            'exam_id',
        ]
        labels = {
            'name': '姓名',
            'gender': '性别',
            'card_type': '证件类型',
            'id_number': '证件号码',
            'phone_number': '手机号',
            'middle_school': '初中毕业学校',
            'subject': '选考科目',
            'photo': '上传个人一寸照片',
            'exam_id': '准考证号',
        }
        widgets = {
            'phone_number': forms.TextInput(attrs={'type': 'number'}),
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'middle_school': forms.TextInput(attrs={'autocomplete': 'off'}),
            'id_number': forms.TextInput(attrs={'autocomplete': 'off'}),
        }
