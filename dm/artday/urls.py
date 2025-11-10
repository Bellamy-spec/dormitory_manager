"""艺术节报名系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 用于报名节目的页面
    path('add_program/', views.add_program, name='add_program'),

    # 显示节目列表的页面
    path('program_list/<str:year>/', views.program_list, name='program_list'),

    # 显示某个具体节目信息的页面
    path('show_program/<int:program_id>/', views.show_program, name='show_program'),

    # 用于报名服装的页面
    path('add_costume/', views.add_costume, name='add_costume'),

    # 显示服装列表的页面
    path('costume_list/<str:year>/', views.costume_list, name='costume_list'),

    # 用于显示某个具体服装信息的页面
    path('show_costume/<int:costume_id>/', views.show_costume, name='show_costume'),

    # 删除节目
    path('delete_program/<int:program_id>/<str:load_to>/', views.delete_program, name='delete_program'),

    # 删除服装
    path('delete_costume/<int:costume_id>/<str:load_to>/', views.delete_costume, name='delete_costume'),

    # 查看节目表演者的页面
    path('see_performer/<int:program_id>/', views.see_performer, name='see_performer'),

    # 查看服装设计师的页面
    path('see_designer/<int:costume_id>/', views.see_designer, name='see_designer'),

    # 编辑节目信息的页面
    path('edit_program/<int:program_id>/<str:program_sec>/', views.edit_program, name='edit_program'),

    # 编辑服装信息的页面
    path('edit_costume/<int:costume_id>/<str:costume_sec>/', views.edit_costume, name='edit_costume'),

    # 增加节目表演者的页面
    path('add_performer/<int:program_id>/', views.add_performer, name='add_performer'),

    # 增加服装设计师的页面
    path('add_designer/<int:costume_id>/', views.add_designer, name='add_designer'),

    # 删除节目表演者
    path('delete_performer/<int:performer_id>/', views.delete_performer, name='delete_performer'),

    # 删除服装设计师
    path('delete_designer/<int:designer_id>/', views.delete_designer, name='delete_designer'),

    # 导出节目单
    path('export_program/<str:year>/', views.export_program, name='export_program'),

    # 导出服装信息
    path('export_costume/<str:year>/', views.export_costume, name='export_costume'),

    # 给服装设置编号
    path('set_num/<int:costume_id>/', views.set_num, name='set_num'),

    # 修改服装信息
    path('change_costume/<str:costume_sec>/', views.change_costume, name='change_costume'),

    # 输入口令页面
    path('change_costume/', views.sec_input, name='sec_input'),

    # 导出服装口令信息
    path('export_sec/<str:year>/', views.export_sec_costume, name='export_sec'),

    # 年份列表
    path('years/', views.years, name='years'),

    # 年份主页
    path('year/<str:year>/', views.year_main, name='year_main'),

    # 输入节目口令
    path('program_sec_input/<str:year>/', views.program_sec_input, name='program_sec_input'),

    # 输入服装口令
    path('costume_sec_input/<str:year>/', views.costume_sec_input, name='costume_sec_input'),

    # 查看节目口令
    path('see_program_sec/<str:year>/', views.see_program_sec, name='see_program_sec'),

    # 查看服装口令
    path('see_costume_sec/<str:year>/', views.see_costume_sec, name='see_costume_sec'),

    # 更新节目口令
    path('update_program_sec/<int:program_id>/', views.update_program_sec, name='update_program_sec'),

    # 更新服装口令
    path('update_costume_sec/<int:costume_id>/', views.update_costume_sec, name='update_costume_sec'),
]
