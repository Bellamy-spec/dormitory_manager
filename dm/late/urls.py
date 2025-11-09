"""迟到记录程序的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有日期的页面
    path('dates/', views.dates, name='dates'),

    # 显示一天的迟到记录
    path('latelist/<int:date_id>/', views.see, name='see'),

    # 新一天的迟到记录
    path('add/', views.add, name='add'),

    # 记录迟到学生
    path('edit/<int:date_id>/', views.edit, name='edit'),

    # 显示班级迟到学生的页面
    path('show/<int:class_id>/<str:late_code>/', views.show_late, name='show'),

    # 新增迟到学生的页面
    path('add_late/<int:class_id>/', views.add_late, name='add_late'),

    # 删除迟到学生的页面
    path('delete/<int:student_id>/', views.delete, name='delete'),
]
