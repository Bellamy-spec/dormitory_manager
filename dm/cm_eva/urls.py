"""班会评价系统的url模式"""
from django.urls import path
from . import views

urlpatterns = [
    # 程序主页
    path('', views.index, name='index'),

    # 登录页面
    path('login/', views.login1, name='login'),

    # 注销登录
    path('logout/', views.logout_view, name='logout'),

    # 设置密码
    path('setpassword/', views.set_pwd, name='set_pwd'),

    # 检查结果上报页面
    path('up_load/<str:gc>/', views.up_load, name='up_load'),

    # 显示单次评价
    path('see_score/<int:score_id>/', views.see_score, name='see_score'),

    # 日期列表
    path('date_list/', views.date_list, name='date_list'),

    # 查看某一天所有班级班会评价情况
    path('day/<str:date_str>/', views.day, name='day'),

    # 月总结主页
    path('mt_main/', views.mt_main, name='mt_main'),

    # 查看某个年级、某个月的班会月总结
    path('mt/<int:grade_num>/<str:ym>/', views.mt, name='mt'),

    # 导出某个年级、某个月的班会月总结
    path('export_mt/<int:grade_num>/<str:ym>/', views.export_mt, name='export_mt'),

    # 删除班会评分记录
    path('delete_score/<int:score_id>/', views.delete_score, name='delete_score'),
]
