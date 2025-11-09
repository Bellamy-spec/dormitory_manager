"""活动报名程序的表单"""
from .models import Activities, Participant
from django import forms


class ActivitiesForm(forms.ModelForm):
    """发布活动的表单"""
    class Meta:
        model = Activities
        fields = ['name', 'tm_str', 'place', 'desc']
        labels = {
            'name': '活动名称',
            'tm_str': '活动时间',
            'place': '活动地点',
            'desc': '活动简介',
        }
        widgets = {
            'desc': forms.Textarea(),
            'tm_str': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class ParticipateForm(forms.ModelForm):
    """参加活动的表单"""
    class Meta:
        model = Participant
        fields = ['department', 'name', 'phone_number']
        labels = {'department': '所属部门', 'name': '姓名', 'phone_number': '手机号'}
