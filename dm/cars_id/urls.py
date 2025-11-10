"""车牌号信息收集系统的url模式"""
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

    # 查看车牌信息
    path('see/', views.see, name='see'),

    # 录入车牌信息
    path('add/', views.add, name='add'),

    # 删除车牌信息
    path('delete/<int:record_id>/', views.delete, name='delete'),

    # 导出车牌信息
    path('export/', views.export, name='export'),

    # 导出含手机号的车牌信息
    path('load/', views.download, name='download'),

    # 查询车牌号信息的链接
    path('find/', views.que, name='que'),
]
