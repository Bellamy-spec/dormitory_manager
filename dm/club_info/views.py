from django.shortcuts import render
from .models import Club, Member
from .tools import DataTool
from .forms import ClubForm, MemberForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.conf import settings

# 实例化数据类
DT = DataTool()


def render_ht(request, template_name, context):
    """重新定义返回网页模板的方法"""
    # 加入选项卡标题
    context.update({'head_title': '{}社团管理系统'.format(settings.USER_NAME)})
    return render(request, template_name, context)


def correct_id(id_number):
    """检查所给的身份证号格式是否合法"""
    # 位数须为18
    if len(id_number) != 18:
        return False

    # 前17位须为数字
    if not id_number[:17].isdigit():
        return False

    # 最后一位须为数字或X
    if not (id_number[17].isdigit() or id_number[17] == 'X'):
        return False

    # TODO:校验
    s = 0
    for i in range(18):
        # 取得每一位上的数字
        if id_number[i].isdigit():
            n = int(id_number[i])
        else:
            n = 10

        # 计算权
        w = 2 ** (17 - i) % 11

        # 累加
        s += n * w

    if s % 11 != 1:
        return False

    # 通过所有检查，格式正确
    return True


# Create your views here.
def index(request):
    """主页"""
    return render_ht(request, 'club_info/index.html', context={
        'is_manager': request.user.username in DT.managers,
        'title': '{}社团管理系统'.format(settings.USER_NAME),
    })


def see(request):
    """查看社团信息"""
    # 初始化列表
    clubs = []

    # 遍历所有社团
    for club in Club.objects.all():
        # 生成社团教师字符串
        teachers = []
        for teacher in Member.objects.filter(club_belong=club, tp='社团教师'):
            teachers.append(teacher.name)
        teacher_str = ', '.join(teachers)

        clubs.append((club, teacher_str))

    context = {'clubs': tuple(clubs), 'is_manager': request.user.username in DT.managers}
    return render_ht(request, 'club_info/see.html', context)


def member_info(request, club_id):
    """查看某个社团成员信息"""
    # 取出要查看的社团
    club = Club.objects.get(id=club_id)

    # 取出所有成员
    members = Member.objects.filter(club_belong=club).order_by('tp')

    context = {
        'club': club,
        'members': members,
        'is_manager': request.user.username in DT.managers,
    }
    return render_ht(request, 'club_info/member_info.html', context)


def add_club(request):
    """新建社团"""
    if request.method != 'POST':
        # 未提交数据，创建新的表单
        form = ClubForm()
    else:
        # 对POST提交的数据作出处理
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('club_info:see'))

    return render_ht(request, 'club_info/add_club.html', {'form': form})


def add_member(request):
    """录入社团成员"""
    if request.method != 'POST':
        # 未提交数据，创建新的表单
        form = MemberForm()
    else:
        # 对POST提交的数据作出处理
        form = MemberForm(request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)

            # TODO:验证身份证号是否符合规范
            if not correct_id(new_member.id_number):
                return render_ht(request, 'club_info/add_member.html', context={
                    'form': form, 'err': '身份证号错误！'})

            # 所属社团学生成员数量变化
            club = new_member.club_belong
            if new_member.tp == '社团成员':
                club.nums += 1
                club.save()

            new_member.save()
            return HttpResponseRedirect(reverse('club_info:member_info', args=[club.id]))

    return render_ht(request, 'club_info/add_member.html', {'form': form, 'err': ''})


def delete_member(request, member_id):
    """删除社团成员"""
    # 需要管理员权限
    if request.user.username not in DT.managers:
        raise Http404

    # 取出要删除的成员对象及所属社团对象
    member = Member.objects.get(id=member_id)
    club = member.club_belong

    # 如果成员类别为学生，则社团学生数减1
    if member.tp == '社团成员':
        club.nums -= 1
        club.save()

    # 执行删除操作
    member.delete()

    # 重定向至社团成员信息页
    return HttpResponseRedirect(reverse('club_info:member_info', args=[club.id]))


def delete_club(request, club_id):
    """删除社团"""
    # 需要管理员权限
    if request.user.username not in DT.managers:
        raise Http404

    # 取出要删除的社团
    club = Club.objects.get(id=club_id)

    # 执行删除操作
    club.delete()

    # 重定向至查看页
    return HttpResponseRedirect(reverse('club_info:see'))
