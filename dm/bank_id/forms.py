"""表单"""
from django import forms
from .models import BKRecord


class BKRecordForm(forms.ModelForm):
    """用于填报记录的表单"""
    class Meta:
        model = BKRecord
        fields = ['name', 'work_point', 'id_number', 'bank_id']
        labels = {
            'name': '姓名',
            'work_point': '监考考点',
            'id_number': '身份证号',
            'bank_id': '银行卡号',
        }
        widgets = {
            'bank_id': forms.TextInput(attrs={'id': 'bk', 'oninput': 'show_bank()'}),
        }
