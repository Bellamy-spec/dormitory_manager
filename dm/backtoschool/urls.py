"""返校情况统计程序的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 任务页面
    path('task/<int:task_id>/', views.one_task, name='task'),

    # 班级查看页面
    path('see/<int:class_id>/', views.see_class, name='see'),

    # 班级编辑页
    path('edit/<int:class_id>/<str:err>/', views.edit_class, name='edit'),

    # 新增请假学生的页面
    path('add/<int:class_id>/', views.add_absent_student, name='add_absent'),

    # 删除请假学生
    path('delete/student/<int:student_id>/', views.delete_student, name='delete_student'),

    # 发布任务的页面
    path('public/', views.public_task, name='public'),

    # 删除任务
    path('delete/task/<int:task_id>/', views.delete_task, name='delete_task'),

    # 导出一次返校情况
    path('export/<int:task_id>/', views.export, name='export'),

    # 标记任务为已完成
    path('mark_done/<int:task_id>/', views.mark_done, name='mark_done'),

    # 载入上次请假学生
    path('add_last/<int:cs_id>/', views.add_last, name='add_last'),

    # 增加高三13班
    path('add_13/<int:task_id>/', views.add_13, name='add_13'),
]
