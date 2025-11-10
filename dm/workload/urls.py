"""工作量统计系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 登录页
    path('login/', views.login1, name='login'),

    # 注销登录
    path('logout/', views.logout_view, name='logout'),

    # 设置密码
    path('setpassword/', views.set_pwd, name='set_pwd'),

    # 任务主页
    path('task/<int:task_id>/', views.task_main, name='task_main'),

    # 发布课时量统计任务的页面
    path('public/', views.public, name='public'),

    # 填报页面
    path('send_up/<int:task_id>/', views.send_up, name='send_up'),

    # 已填报教师列表页面
    path('teacher_list/<int:task_id>/', views.teacher_list, name='teacher_list'),

    # 记录详情页面
    path('show_record/<int:record_id>/', views.show_record, name='show_record'),

    # 删除任务页面
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    # 删除记录页面
    path('delete_record/<int:record_id>/', views.delete_record, name='delete_record'),

    # 导出数据
    path('export/<int:task_id>/', views.export, name='export'),

    # 添加代课情况的页面
    path('add_sub/<int:record_id>/', views.add_sub, name='add_sub'),

    # 删除代课情况
    path('delete_sub/<int:sb_id>/', views.delete_sub, name='delete_sub'),

    # 更改上课周数
    path('change_weeks/<int:task_id>/', views.change_weeks, name='change_weeks'),
]
