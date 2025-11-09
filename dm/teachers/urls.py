"""教师信息收集系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 录入教师信息
    path('add/', views.add, name='add'),

    # 查看教师信息
    path('see/', views.see, name='see'),

    # 删除教师信息
    path('delete/<int:teacher_id>/', views.delete, name='delete'),

    # 导出教师信息数据
    path('export/', views.load, name='load'),
]
