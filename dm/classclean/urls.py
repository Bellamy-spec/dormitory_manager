"""班级卫生记分程序的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 分年级日期列表页面
    path('dates/<int:grade_num>/', views.show_dates, name='dates'),

    # 分年级分日期查看
    path('look/<int:grade_num>/<str:date_str>/', views.show_records, name='look'),

    # 新增记录
    path('add/', views.add_record, name='add'),

    # 删除记录
    path('delete/<record_id>/', views.delete_record, name='delete'),

    # 月总结主页
    path('mt/', views.mt_main, name='mt_main'),

    # 导出月总结
    path('export_mt/<int:grade_num>/<str:month_str>/', views.export_mt, name='export_mt'),

    # 查看月总结
    path('show_mt/<int:grade_num>/<str:month_str>/', views.show_mt, name='show_mt'),

    # 学生会检查填报页面
    path('up_load/<str:gc>/', views.up_load, name='up_load'),

    # 学生会检查评分查看页面
    path('see_score/<int:score_id>/', views.see_score, name='see_score'),

    # 学生会检查结果日期列表页面
    path('su_dl/', views.su_dl, name='su_dl'),

    # 学生会检查结果一日页面
    path('su_day/<str:date_str>/', views.su_day, name='su_day'),

    # 删除评分对象
    path('del_score/<int:score_id>/', views.del_score, name='del_score'),

    # 结果公示年级列表页面
    path('pub_grade_list/', views.pub_grade_list, name='pub_grade_list'),

    # 某年级某天结果公示
    path('pub/<int:grade_num>/<str:date_str>/', views.pub, name='pub'),

    # 某年级某天结果公示导出
    path('pub_export/<int:grade_num>/<str:date_str>/', views.pub_export, name='pub_export'),

    # 仪容仪表检查填报页面
    path('yryb_upload/<str:gc>/', views.yryb_upload, name='yryb_upload'),

    # 仪容仪表检查记录显示
    path('see_yryb_record/<int:yryb_id>/', views.see_yryb_record, name='see_yryb_record'),

    # 仪容仪表检查结果主页
    path('yryb_main/', views.yryb_main, name='yryb_main'),

    # 查看某年级某一天仪容仪表检查不合格名单
    path('yryb_day/<int:grade_num>/<str:date_str>/', views.yryb_day, name='yryb_day'),

    # 删除仪容仪表检查记录
    path('delete_yryb_record/<int:yryb_id>/', views.delete_yryb_record, name='delete_yryb_record'),

    # 导出仪容仪表不合格名单
    path('yryb_export/<int:grade_num>/<str:date_str>/', views.yryb_export, name='yryb_export'),
]
