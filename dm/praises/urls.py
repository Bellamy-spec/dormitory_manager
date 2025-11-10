# coding=utf-8
"""期末评优评先上报系统的url模式"""
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

    # 发布新任务
    path('public_task/', views.public_task, name='public_task'),

    # 任务查看页面
    path('see_task/<int:task_id>/', views.see_task, name='see_task'),

    # 更改任务活跃状态
    path('change_active/<int:task_id>/', views.change_active, name='change_active'),

    # 删除任务
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    # 班级提交查看
    path('see_class/<int:class_id>/', views.see_class, name='see_class'),

    # 下载获奖学生名单模板
    path('download_temp/<int:task_id>/', views.download_temp, name='download_temp'),

    # 班级列表
    path('class_list/<int:task_id>/', views.class_list, name='class_list'),

    # 删除班级提交对象
    path('delete_class/<int:class_id>/', views.delete_class, name='delete_class'),

    # 修改证书日期
    path('change_cert_date/<int:task_id>/', views.change_cert_date, name='change_cert_date'),

    # 删除获奖学生对象
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),

    # 单个添加获奖学生
    path('add_student/<int:class_id>/', views.add_student, name='add_student'),

    # 下载学生的电子获奖证书
    path('download_cert/<int:student_id>/', views.download_cert, name='download_cert'),

    # 以压缩包形式导出班级获奖电子证书
    path('export_class_cert/<int:class_id>/', views.export_class_cert, name='export_class_cert'),

    # 以压缩包形式导出班级获奖名单
    path('export_task_xlsx/<int:task_id>/', views.export_task_xlsx, name='export_task_xlsx'),

    # 导出获奖证书打印模板
    path('export_print_temp/<int:task_id>/', views.export_print_temp, name='export_print_temp'),
]
