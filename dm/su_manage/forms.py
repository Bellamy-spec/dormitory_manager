"""表单"""
from django import forms
from .models import SchoolYear, Department, Member


class SchoolYearForm(forms.ModelForm):
    """用于设置学年的表单"""
    class Meta:
        model = SchoolYear
        fields = ['start_date', 'end_date']
        labels = {'start_date': '开始日期', 'end_date': '结束日期'}
        widgets = {
            'start_date': forms.TextInput(attrs={'type': 'date', 'id': 'sd',
                                                 'onchange': 'config_end_year()'}),
            'end_date': forms.TextInput(attrs={
                'type': 'date',
                # Duck不必
                # 'min': date(date.today().year + 1, 1, 1),
                # 'max': date(date.today().year + 1, 12, 31),
                'id': 'ed',
            }),
        }


class AddDepartmentForm(forms.ModelForm):
    """用于新增部门的表单"""
    class Meta:
        model = Department
        fields = ['name', 'desc', 'code_int', 'work_abst2', 'head_name']
        labels = {
            'name': '部门名称',
            'desc': '部门介绍',
            'code_int': '部门代号',
            # 'work_abst1': '是否承担早操工作',
            'work_abst2': '是否承担课间操工作',
            'head_name': '干部称呼',
        }
        widgets = {
            'code_int': forms.TextInput(attrs={'type': 'number', 'min': 0, 'max': 99}),
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
        }


class FileUploadForm(forms.Form):
    """模板批量添加成员表单"""
    file = forms.FileField(label='批量导入成员')


class FbdpForm(forms.ModelForm):
    """用于完善部门介绍的表单"""
    class Meta:
        model = Department
        fields = ['desc']
        labels = {'desc': ''}


class MemberForm(forms.ModelForm):
    """用于单个新增或修改成员的表单"""
    class Meta:
        model = Member
        fields = ['department', 'name', 'class_and_grade', 'level',
                  'main_work', 'work_abst2']
        labels = {
            'department': '部门',
            # 'num': '编号',
            'name': '姓名',
            'class_and_grade': '所在班级',
            'level': '职级',
            'main_work': '工作职责',
            # 'work_abst1': '是否不上早操',
            'work_abst2': '是否课间操工作人员',
        }
        widgets = {
            'department': forms.Select(attrs={'id': 'dp', 'onchange': 'set_check()'}),
            'main_work': forms.Textarea(),
            # 'work_abst1': forms.TextInput(attrs={'id': 'wa1', 'type': 'checkbox'}),
            'work_abst2': forms.TextInput(attrs={'id': 'wa2', 'type': 'checkbox'}),
        }


class ConfigWorkerForm(forms.Form):
    """模板批量更改课间操工作人员"""
    file = forms.FileField(label='批量更改课间操工作人员')
