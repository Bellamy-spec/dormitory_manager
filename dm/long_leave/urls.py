"""两操长期假人员管理系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 上级页
    path('index_out/', views.index_out, name='index_out'),

    # 主页
    path('', views.index, name='index'),

    # 管理页
    path('manage/', views.see, name='manage'),

    # 新增页
    path('add/', views.add, name='add'),

    # 删除记录（提前结束）
    path('delete/<int:r_id>/', views.delete, name='delete'),

    # 改变日期和请假类型的页面
    path('change/<int:r_id>/', views.change_date, name='change'),

    # 查看页
    path('look/', views.look, name='look'),

    # 导出
    path('export/', views.export, name='export'),

    # 每日请假与在校人员
    path('daily/', views.daily, name='daily'),

    # 上报页面
    path('send_up/', views.send_up, name='send_up'),

    # 日期列表页面
    path('dates/<int:grade_num>/', views.dates, name='dates'),

    # 年级列表页面
    path('grades/', views.grades, name='grades'),

    # 一个年级一天的页面
    path('records/<int:grade_num>/<str:date_str>/', views.one_day, name='show_records'),

    # 查看班级具体情况页面
    path('class/<int:cs_id>/', views.show_cs, name='show_cs'),

    # 删除请假学生的链接
    path('delete_st/<int:st_id>/', views.delete_st, name='delete_st'),

    # 用于更改已提交班级应到人数的页面
    path('change_total/<int:cs_id>/', views.change_total, name='change_total'),

    # 用于已提交班级新增请假学生的页面
    path('add_st/<int:cs_id>/', views.add_st, name='add_st'),

    # 获取某个班级最近一次请假学生
    path('get_last/<str:cs_str>/<int:total>/', views.get_last, name='get_last'),
]
