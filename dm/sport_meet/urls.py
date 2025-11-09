"""运动会报名系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 报名项目的页面
    path('put_name/', views.put_name, name='put_name'),

    # 查询及查看运动员的页面
    path('que/', views.que, name='que'),

    # 删除项目及相应的报名对象
    path('delete_item/<int:athlete_id>/<str:athlete_pwd>/<int:item_idx>/<int:code>/<str:year>/',
         views.delete_item, name='delete_item'),

    # 年份列表
    path('yl/', views.yl, name='yl'),

    # 管理端主页
    path('admin/<str:year>/', views.admin, name='admin'),

    # 显示运动员列表
    path('athletes/<str:year>/', views.athletes, name='athletes'),

    # 班级登录页面
    path('class_login/', views.class_login, name='class_login'),

    # 删除运动员或更新运动员口令
    path('delete_athlete/<int:athlete_id>/<str:athlete_pwd>/<int:code>/',
         views.delete_athlete, name='delete_athlete'),

    # 项目分组
    path('make_group/<str:year>/', views.make_group, name='make_group'),

    # 编号与姓名对照
    path('num_name/<str:year>/', views.num_name, name='num_name'),

    # 查看报名记录
    path('show_put_name/', views.show_put_name, name='show'),
]
