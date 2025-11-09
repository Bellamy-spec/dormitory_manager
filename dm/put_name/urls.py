"""活动报名系统的url模式"""
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

    # 发布活动页面
    path('public/', views.public, name='public'),

    # 查看活动页面
    path('look/<int:activity_id>/', views.one_activity, name='look'),

    # 管理活动页面
    path('manage/<int:activity_id>/', views.manage, name='manage'),

    # 开始或恢复活动报名
    path('sted/<int:activity_id>/', views.start_or_end, name='sted'),

    # 删除活动
    path('delete/<int:activity_id>/', views.delete_activity, name='delete'),

    # 修改活动
    path('edit/<int:activity_id>/', views.edit_activity, name='edit'),

    # 活动报名
    path('apply/<int:activity_id>/', views.apply, name='apply'),

    # 查看报名情况
    path('see/<int:activity_id>/', views.see_part, name='see'),

    # 取消报名
    path('cancel/<int:part_id>/', views.cancel, name='cancel'),
]
