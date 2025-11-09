"""银行卡信息收集系统的url"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 登录页面
    path('login/', views.login1, name='login'),

    # 注销登录
    path('logout/', views.logout_view, name='logout'),

    # 设置密码
    path('setpassword/', views.set_pwd, name='set_pwd'),

    # 查看页面
    path('review/', views.review, name='review'),

    # 删除记录
    path('delete/<int:record_id>/', views.delete, name='delete'),

    # 填报信息
    path('send_up/', views.send_up, name='send_up'),

    # 导出信息
    path('export/', views.export, name='export'),
]
