"""社团管理系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 查看社团信息
    path('see/', views.see, name='see'),

    # 查看社团成员信息
    path('members/<int:club_id>/', views.member_info, name='member_info'),

    # 用于新建社团的页面
    path('add_club/', views.add_club, name='add_club'),

    # 用于录入社团成员的页面
    path('add_member/', views.add_member, name='add_member'),

    # 删除社团成员
    path('delete_member/<member_id>/', views.delete_member, name='delete_member'),

    # 删除社团
    path('delete_club/<club_id>/', views.delete_club, name='delete_club'),
]
