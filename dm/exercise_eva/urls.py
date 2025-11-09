# -*- coding: utf-8 -*-
"""课间操评价系统的url模式"""
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

    # 短假学生管理
    path('short_abst_manage/', views.short_abst_manage, name='short_abst_manage'),

    # 短假登记进入页面
    path('load_short_in/', views.load_short_in, name='load_short_in'),

    # 短假学生登记
    path('load_short_abst/', views.load_short_abst, name='load_short_abst'),

    # 删除短假学生
    path('del_short_abst/<int:student_id>/', views.del_short_abst, name='del_short_abst'),

    # 短假学生日期列表
    path('short_abst_dates/', views.short_abst_dates, name='short_abst_dates'),

    # 按日期查看短假学生
    path('date_short_abst/<str:date_str>/', views.short_abst_manage, name='date_short_abst'),

    # 检查结果上报页面
    path('up_load/', views.up_load, name='up_load'),

    # 评价结果日期列表
    path('score_dates/', views.score_dates, name='score_dates'),

    # 评价结果查看页面
    path('see_score/<str:date_str>/', views.see_score, name='see_score'),

    # 删除课间操评价结果
    path('del_score/<int:score_id>/', views.del_score, name='del_score'),

    # 月总结主页
    path('mt_main/', views.mt_main, name='mt_main'),

    # 月总结
    path('mt/<int:grade_num>/<str:ym>/', views.mt, name='mt'),

    # 导出月总结
    path('export_mt/<int:grade_num>/<str:ym>/', views.export_mt, name='export_mt'),

    # 节能检查结果上报
    path('eco_upload/', views.eco_upload, name='eco_upload'),

    # 节能记录日期列表
    path('eco_dates/', views.eco_dates, name='eco_dates'),

    # 查看一天节能记录情况
    path('see_eco/<str:date_str>/', views.see_eco, name='see_eco'),

    # 删除节能记录
    path('del_eco/<int:score_id>/', views.del_eco, name='del_eco'),
]
