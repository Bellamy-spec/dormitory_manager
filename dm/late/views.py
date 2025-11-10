from django.shortcuts import render
from .tools import DataTool
from .models import DateRecord, ClassRecord, LateStudent
from django.http import Http404, HttpResponseRedirect
import datetime
from django.urls import reverse
from .forms import StudentForm
from django.conf import settings

# Create your views here.
# 实例化工具类
DT = DataTool()


def render_ht(request, template_name, context):
    """重新定义返回网页模板的方法"""
    # 加入选项卡标题
    context.update({'head_title': '{}学生日常行为规范管理系统'.format(settings.USER_NAME)})
    return render(request, template_name, context)


def get_late_students(class_obj, tm):
    """以列表形式返回班级对象的迟到学生"""
    late_students = []
    students = LateStudent.objects.filter(class_belong=class_obj, tm=tm)
    for student in students:
        late_students.append(student.name)
    return late_students


def all_date():
    """获取所有日期"""
    dates_all = []
    for d in DateRecord.objects.all():
        dates_all.append(d.date)
    return dates_all


def index(request):
    """主页"""
    context = {
        'title': '{}迟到学生记录系统'.format(settings.USER_NAME),
        'is_manager': request.user.username in DT.managers,
    }
    return render_ht(request, 'late/index.html', context)


def dates(request):
    """显示所有日期的页面"""
    # 获取所有日期对象
    date_objects = DateRecord.objects.all()

    context = {'title': '选择日期', 'dates': date_objects}
    return render_ht(request, 'late/dates.html', context)


def see(request, date_id):
    """查看某一天的迟到记录"""
    # 获取日期对象
    date_object = DateRecord.objects.get(id=date_id)

    # 获取班级对象
    class_objects = ClassRecord.objects.filter(date_happened=date_object)

    # 班级排序
    class_objects = list(class_objects)
    class_objects.sort(key=lambda x: x.cs)
    class_objects.sort(key=lambda x: x.grade_num)
    class_objects = tuple(class_objects)

    context = {
        'title': '{}迟到学生记录'.format(date_object.date_str),
        'css': class_objects,
        'is_manager': request.user.username in DT.managers,
        'late_only': False,
    }
    return render_ht(request, 'late/see.html', context)


def add(request):
    """新一天的迟到记录"""
    # 非管理员无此权限
    if request.user.username not in DT.managers:
        raise Http404

    # 生成班级字符串
    css = []
    for grade in DT.grades_num.keys():
        for cs in DT.cs_dict.values():
            css.append((grade + cs, cs))
    css = tuple(css)

    if request.method == 'POST':
        # 对POST提交的数据作出处理
        new_date = DateRecord()

        # 从前端获取日期
        new_date.date = request.POST.get('dt', '')

        # 检查日期是否重复
        if new_date.date in all_date():
            return render_ht(request, 'late/add.html', context={
                'css': css,
                'enter_code': ('4班', '8班', '12班'),
                'err': '该日期已有记录，请在查看页中直接修改',
            })

        # 生成日期字符串
        new_date.date_str = datetime.datetime.strftime(new_date.date, '%Y-%m-%d')

        # 保存
        new_date.save()

        # TODO:创建班级对象
        for gc in css:
            # 名称
            class_obj = ClassRecord()
            class_obj.class_and_grade = gc[0]
            class_obj.grade = gc[0][:2]
            class_obj.grade_num = DT.grades_num[class_obj.grade]
            class_obj.cs = int(DT.num_regex.findall(gc[0])[0])

            # 所属日期
            class_obj.date_happened = new_date

            # 从前端获取是否有人迟到
            if request.POST.get(gc, ''):
                class_obj.has_late = True
            else:
                class_obj.has_late = False

            # 保存创建好的班级对象
            class_obj.save()

        # 跳转到下一步
        return HttpResponseRedirect(reverse('late:edit', args=[new_date.id]))

    # 对于get方法，创建新的表单
    return render_ht(request, 'late/add.html', context={
        'css': css,
        'enter_code': ('4班', '8班', '12班'),
        'err': '',
    })


def edit(request, date_id):
    """记录迟到学生"""
    # 取出日期及当天有迟到学生的班级
    date_obj = DateRecord.objects.get(id=date_id)
    css_late = ClassRecord.objects.filter(date_happened=date_obj, has_late=True)

    # 制定标题
    title = '记录{}迟到学生'.format(date_obj.date_str)

    context = {
        'title': title,
        'css': css_late,
        'is_manager': request.user.username in DT.managers,
        'late_only': True,
    }
    return render_ht(request, 'late/see.html', context)


def show_late(request, class_id, late_code):
    """显示一个班级的迟到学生"""
    if late_code == 'a':
        late_only = True
    else:
        late_only = False

    # 取出对应班级及迟到学生
    class_obj = ClassRecord.objects.get(id=class_id)
    late_students = LateStudent.objects.filter(class_belong=class_obj)

    # 制定标题
    title = '{}{}迟到学生'.format(
        class_obj.class_and_grade, class_obj.date_happened.date_str)

    context = {
        'title': title,
        'cs': class_obj,
        'late_students': late_students,
        'late_only': late_only,
    }
    return render_ht(request, 'late/show_late.html', context)


def add_late(request, class_id):
    """新增迟到学生"""
    # 非管理员无此权限
    if request.user.username not in DT.managers:
        raise Http404

    # 取出对应的班级对象
    class_obj = ClassRecord.objects.get(id=class_id)

    if request.method != 'POST':
        # 未提交数据，创建一个新表单
        form = StudentForm()
    else:
        # 对POST提交的数据作出处理
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save(commit=False)

            # 关联对应班级
            new_student.class_belong = class_obj

            # 保存对象
            new_student.save()

            # 更新母对象属性
            if new_student.tm == '早上':
                if class_obj.late_students_am == '无':
                    class_obj.late_students_am = new_student.name
                else:
                    class_obj.late_students_am += ',' + new_student.name
            elif new_student.tm == '中午':
                if class_obj.late_students_pm == '无':
                    class_obj.late_students_pm = new_student.name
                else:
                    class_obj.late_students_pm += ',' + new_student.name

            # 母对象迟到人数及是否迟到标志
            class_obj.late_num += 1
            class_obj.has_late = True

            # 保存母对象所做更改
            class_obj.save()

            return HttpResponseRedirect(reverse('late:show', args=[class_id]))

    # 制定标题
    title = '新增{}{}迟到学生'.format(
        class_obj.class_and_grade, class_obj.date_happened.date_str)
    return render_ht(request, 'late/add_late.html', context={
        'title': title, 'form': form, 'cs_id': class_id})


def delete(request, student_id):
    """删除迟到的学生"""
    # 非管理员无此权限
    if request.user.username not in DT.managers:
        raise Http404

    # 先取出要删除的学生对象，其时间类型、姓名及母对象
    student_obj = LateStudent.objects.get(id=student_id)
    class_obj = student_obj.class_belong
    tm = student_obj.tm

    # 执行删除操作
    student_obj.delete()

    # 母对象须相应作出修改
    late_changed = get_late_students(class_obj, tm)
    if tm == '早上':
        if late_changed:
            class_obj.late_students_am = ','.join(late_changed)
        else:
            class_obj.late_students_am = '无'
    elif tm == '中午':
        if late_changed:
            class_obj.late_students_pm = ','.join(late_changed)
        else:
            class_obj.late_students_pm = '无'

    # 人数及标志修改
    class_obj.late_num -= 1
    if class_obj.late_num == 0:
        class_obj.has_late = False

    # 保存母对象所做修改
    class_obj.save()

    return HttpResponseRedirect(reverse('late:show', args=[class_obj.id]))
