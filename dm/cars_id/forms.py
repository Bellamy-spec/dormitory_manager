"""车牌统计系统的表单"""
from django import forms
from .models import CarRecord


class CarForm(forms.ModelForm):
    """用于填写收集车牌信息的表单"""
    class Meta:
        model = CarRecord
        fields = ['name', 'tp', 'phone_number', 'car1']
        labels = {
            'name': '车主姓名',
            'tp': '人员类别',
            'phone_number': '手机号',
            'car1': '车牌号1',
        }
