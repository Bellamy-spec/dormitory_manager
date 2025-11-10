from django.shortcuts import render
from .models import Activities, Participant
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.urls import reverse
from django.contrib.auth.views import login_required
from .forms import ActivitiesForm, ParticipateForm
import datetime
from .tools import DataTool
from django.conf import settings


# 实例化数据类
DT = DataTool()


def render_ht(request, template_name, context):
    """重新定义返回网页模板的方法"""
    # 加入选项卡标题
    context.update({'head_title': '{}活动报名管理系统'.format(settings.USER_NAME)})
    return render(request, template_name, context)


def get_phone_number_by_activity(activity):
    """取得一个活动所有报名者的手机号"""
    # 初始化手机号列表
    phone_numbers = []

    # 循环遍历报名者，记录手机号
    for part in Participant.objects.filter(activity_belong=activity):
        phone_numbers.append(part.phone_number)

    return phone_numbers


# Create your views here.
def index(request):
    """主页"""
    for activity in Activities.objects.all():
        # 过期活动强制结束
        if activity.tm < datetime.datetime.now(tz=DT.tz):
            activity.out_of_date = True
            activity.active = False
            activity.save()

    # 取出所有进行中、已结束活动
    context = {
        'active': Activities.objects.filter(active=True),
        'inactive': Activities.objects.filter(active=False),
        'title': '{}活动报名系统'.format(settings.USER_NAME),
    }
    return render_ht(request, 'put_name/index.html', context)


def login1(request):
    """登录页"""
    if request.method == 'POST':
        # 对POST提交的数据作出处理
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)

            # 登录成功之后重定向到主页
            return HttpResponseRedirect(reverse('put_name:index'))
        else:
            return render_ht(request, 'put_name/login.html', {'err': '用户名或密码错误！'})

    return render_ht(request, 'put_name/login.html', {'err': ''})


def logout_view(request):
    """注销登录"""
    logout(request)
    return HttpResponseRedirect(reverse('put_name:index'))


@login_required()
def set_pwd(request):
    """修改密码"""
    if request.method == 'POST':
        pwd = request.POST.get('old', '')
        if not authenticate(username=request.user.username, password=pwd):
            return render_ht(request, 'put_name/set_pwd.html', {'err': '原密码不正确'})
        if request.POST.get('new', '') != request.POST.get('new_again', ''):
            return render_ht(request, 'put_name/set_pwd.html', {'err': '两次输入的密码不一致'})

        # 修改密码
        new_pwd = request.POST.get('new', '')
        request.user.set_password(new_pwd)
        request.user.save()
        update_session_auth_hash(request, request.user)

        # 退出登录然后重新登录
        logout(request)
        return render_ht(request, 'put_name/login.html', {'err': '密码已修改成功，请重新登录'})

    return render_ht(request, 'put_name/set_pwd.html', {'err': ''})


@ login_required()
def public(request):
    """发布活动的页面"""
    if request.method != 'POST':
        # 未提交数据，创建新的表单
        form = ActivitiesForm()
    else:
        # 对POST提交的数据作出处理
        form = ActivitiesForm(request.POST)
        if form.is_valid():
            new_activity = form.save(commit=False)

            # 检测活动时间
            new_activity.tm = datetime.datetime.strptime(new_activity.tm_str, '%Y-%m-%dT%H:%M')
            if new_activity.tm <= datetime.datetime.now():
                return render_ht(request, 'put_name/public.html', context={
                    'form': form, 'err': '活动时间不能早于当前时间'})

            # 关联发布者
            new_activity.owner = request.user

            # 保存对象，重定向至主页
            new_activity.save()
            return HttpResponseRedirect(reverse('put_name:index'))

    return render_ht(request, 'put_name/public.html', {'form': form, 'err': ''})


def one_activity(request, activity_id):
    """查看活动详情"""
    # 取出对应活动
    activity = Activities.objects.get(id=activity_id)

    # 格式化显示日期
    ac_date = datetime.datetime.strftime(activity.tm.astimezone(DT.tz), '%Y年%m月%d日%H:%M')

    # 访问者
    looker = request.user

    return render_ht(request, 'put_name/look.html', context={
        'ac': activity,
        'ac_date': ac_date,
        'is_manager': looker.username in DT.managers or looker == activity.owner,
    })


@ login_required()
def manage(request, activity_id):
    """活动管理"""
    # 取出对应的活动
    activity = Activities.objects.get(id=activity_id)

    # 除管理员和发布者以外无权限访问此页
    if not (request.user.username in DT.managers or request.user == activity.owner):
        raise Http404

    # 确定管理者类型，是否能够深度管理
    if request.user == activity.owner:
        deep_manage = True
    else:
        deep_manage = False

    # 格式化显示日期
    ac_date = datetime.datetime.strftime(activity.tm.astimezone(DT.tz), '%Y年%m月%d日%H:%M')

    context = {'ac': activity, 'deep': deep_manage, 'ac_date': ac_date}
    return render_ht(request, 'put_name/manage.html', context)


@ login_required()
def start_or_end(request, activity_id):
    """活动开始或结束报名"""
    # 取出对应的活动
    activity = Activities.objects.get(id=activity_id)

    # 除管理员和发布者以外无权限访问此页
    if not (request.user.username in DT.managers or request.user == activity.owner):
        raise Http404

    # 活跃状态下结束，非活跃状态下开始
    activity.active = not activity.active
    activity.save()

    # 重定向至管理页
    return HttpResponseRedirect(reverse('put_name:manage', args=[activity_id]))


@login_required()
def delete_activity(request, activity_id):
    """删除活动"""
    # 取出要删除的活动
    activity = Activities.objects.get(id=activity_id)

    # 除管理员和发布者以外无权限访问此页
    if not (request.user.username in DT.managers or request.user == activity.owner):
        raise Http404

    # 执行删除操作
    activity.delete()

    # 重定向至主页
    return HttpResponseRedirect(reverse('put_name:index'))


@ login_required()
def edit_activity(request, activity_id):
    """编辑活动"""
    # 取出要编辑的活动
    activity = Activities.objects.get(id=activity_id)

    # 除管理员和发布者以外无权限访问此页
    if not (request.user.username in DT.managers or request.user == activity.owner):
        raise Http404

    if request.method != 'POST':
        # 初次请求，使用当前对象填充表单
        form = ActivitiesForm(instance=activity)
    else:
        # 对POST提交的数据作出处理
        form = ActivitiesForm(instance=activity, data=request.POST)
        if form.is_valid():
            changed = form.save(commit=False)

            # 检测活动时间
            changed.tm = datetime.datetime.strptime(changed.tm_str, '%Y-%m-%dT%H:%M')
            if changed.tm <= datetime.datetime.now():
                return render_ht(request, 'put_name/change.html', context={
                    'form': form, 'err': '活动时间不能早于当前时间', 'ac': activity})

            # TODO：修改原对象各项属性
            activity.name = changed.name
            activity.tm = changed.tm
            activity.place = changed.place
            activity.desc = changed.desc

            # 保存活动，重定向至活动详情页
            activity.save()
            return HttpResponseRedirect(reverse('put_name:look', args=[activity_id]))

    return render_ht(request, 'put_name/change.html', {'form': form, 'err': '', 'ac': activity})


def apply(request, activity_id):
    """活动报名页"""
    # 取出要报名的活动
    ac = Activities.objects.get(id=activity_id)

    # 非活跃状态下活动不可访问此页
    if not ac.active:
        return Http404

    # 格式化显示日期
    ac_date = datetime.datetime.strftime(ac.tm.astimezone(DT.tz), '%Y年%m月%d日%H:%M')

    if request.method != 'POST':
        # 未提交数据，创建新的表单
        form = ParticipateForm()
    else:
        # 对POST提交的数据作出处理
        form = ParticipateForm(request.POST)
        if form.is_valid():
            new_part = form.save(commit=False)

            # 校验手机号
            if not new_part.phone_number.isdigit() or len(new_part.phone_number) != 11:
                return render_ht(request, 'put_name/apply.html', context={
                    'ac': ac,
                    'ac_date': ac_date,
                    'form': form,
                    'err': '请填写正确的手机号',
                })

            # TODO:检查此人是否已报名
            if new_part.phone_number in get_phone_number_by_activity(ac):
                return render_ht(request, 'put_name/apply.html', context={
                    'ac': ac,
                    'ac_date': ac_date,
                    'form': form,
                    'err': '手机号{}的用户已报名参加此活动，请勿重复报名'.format(new_part.phone_number),
                })

            # 报名者关联活动
            new_part.activity_belong = ac

            # 保存报名者
            new_part.save()

            # 母对象报名人数加一
            ac.num += 1
            ac.save()

            # 成功提示
            return render_ht(request, 'put_name/done.html', {'ac': ac})

    return render_ht(request, 'put_name/apply.html', {
        'ac': ac, 'ac_date': ac_date, 'form': form, 'err': ''})


def see_part(request, activity_id):
    """查看报名情况"""
    # 取出对应的活动
    ac = Activities.objects.get(id=activity_id)

    # 取出该活动的所有参与者
    parts = Participant.objects.filter(activity_belong=ac)

    context = {'ac': ac, 'parts': parts}
    return render_ht(request, 'put_name/see.html', context)


def cancel(request, part_id):
    """取消报名"""
    # 取出要取消的报名者及其所属活动
    part = Participant.objects.get(id=part_id)
    ac = part.activity_belong

    # 执行删除操作
    part.delete()

    # 活动人数减1，保存
    ac.num -= 1
    ac.save()

    # 重定向到报名信息页
    return HttpResponseRedirect(reverse('put_name:see', args=[ac.id]))
