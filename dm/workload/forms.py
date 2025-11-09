"""表单"""
from django import forms
from .models import Task, WorkloadRecord, SubLesson


class TaskForm(forms.ModelForm):
    """用于发布课时量统计任务的表单"""
    class Meta:
        model = Task
        fields = ['month', 'weeks', 'grade']
        labels = {'month': '请选择月份', 'weeks': '请设置上课周数', 'grade': '请选择年级'}
        widgets = {
            'grade': forms.Select(attrs={'id': 'grade'}),
        }


class WorkloadForm(forms.ModelForm):
    """用于填报课时量的表单"""
    class Meta:
        model = WorkloadRecord
        fields = ['name', 'subject', 'week_plans', 'week_lessons', 'morning_lessons',
                  'evening_lessons']
        labels = {
            'name': '姓名',
            'subject': '所教学科',
            # 'css': '所教班级',
            'week_plans': '周教案数',
            'week_lessons': '周课时数',
            'morning_lessons': '早辅导次数',
            'evening_lessons': '晚自习次数',
        }
        widgets = {
            # 'css': forms.Textarea(attrs={
            #     'placeholder': '如教多个班级，请用"/"隔开，如：1/2/3/4',
            #     'rows': '2',
            #     'id': 'csn',
            #     'onchange': 'show_weeks()',
            # }),
            'week_plans': forms.TextInput(attrs={'onchange': 'show_weeks()', 'id': 'wp'}),
            'week_lessons': forms.TextInput(attrs={'onchange': 'show_weeks()', 'id': 'wl'}),
        }


class AddSubForm(forms.ModelForm):
    """用于添加代课记录的表单"""
    class Meta:
        model = SubLesson
        fields = ['sub_time', 'sub_teacher', 'sub_class', 'sub_lessons']
        labels = {
            'sub_time': '代课时间',
            'sub_teacher': '被代课教师',
            'sub_class': '代课班级',
            'sub_lessons': '代课节数',
        }


class ChangeWeeksForm(forms.ModelForm):
    """用于更改上课周数的表单"""
    class Meta:
        model = Task
        fields = ['weeks']
        labels = {'weeks': '重新设置上课周数'}
