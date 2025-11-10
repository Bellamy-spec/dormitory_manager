"""dm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # 管理页
    path('admin/', admin.site.urls),

    # 导航页
    url(r'^$', views.index_out, name='index_out'),

    # 首页
    path('index/', views.index, name='index'),

    # 显示所有扣分记录的页面
    path('records/', views.all_records, name='records'),

    # 新增扣分记录的页面
    path('add/', views.new_record, name='add'),

    # 显示某一天扣分记录的页面
    path('records/<int:year>-<int:month>-<int:day>/',
         views.records_by_date, name='records_by_date'),

    # 显示所有日期的页面
    path('dates/', views.show_dates, name='dates'),

    # 登录页面
    path('login/', views.login1, name='login'),

    # 注销登录
    path('logout/', views.logout_view, name='logout'),

    # 设置密码
    path('setpassword/', views.set_pwd, name='set_pwd'),

    # 删除记录
    path('delete/<int:record_id>/', views.delete_record, name='delete'),

    # 分年级页面
    path('grade/', views.grades, name='grades'),

    # 分年级日期页面
    path('grade/<int:grade>/', views.show_dates, name='grade_dates'),

    # 分年级某一天
    path('grade/<int:grade>/<str:date_str>/', views.show_records, name='show_records'),

    # 导出一个年级某一天
    path('download/<int:grade>/<str:date_str>/', views.export_excel, name='download'),

    # 分年级全部
    path('grade/all/<int:grade>/', views.show_all_by_grade, name='grade_all'),

    # 导出年级全部
    path('download/<int:grade>/', views.export_grade_all, name='download_grade_all'),

    # 分年级某一天分性别
    path('grade/<int:grade>/<str:date_str>/<str:gender>/', views.show_records,
         name='show_gender_records'),

    # 分年级某一天分性别导出
    path('download/<int:grade>/<str:date_str>/<str:gender>/', views.export_excel,
         name='download_gender'),

    # 修改记录
    path('change/<int:record_id>/', views.change_record, name='change'),

    # 月总结主页
    path('monthtogether/', views.month_together, name='month_together'),

    # 导出一个年级某个月的月总结
    path('monthtogether/<int:grade>/<str:month_str>/', views.export_grade_month,
         name='export_monthtogether'),

    # 查看一个年级某个月的月总结
    path('monthsummary/<int:grade>/<str:month_str>/', views.show_grade_month,
         name='show_monthtogether'),

    # 查看一个年级某个月的月总结统计图表
    path('month_visual/<int:grade>/<str:month_str>/', views.visual_grade_month,
         name='visual_monthtogether'),

    # 查看一个班大数据统计情况
    path('visual_class/<str:gc_str>/<str:month_str>/', views.visual_class,
         name='visual_class'),

    # 满意度调查主页
    path('advice/', views.advice, name='advice'),

    # 发布调查的页面
    path('add_investigation/', views.add_investigation, name='add_investigation'),

    # 学年选择页面
    path('syl/', views.syl, name='syl'),

    # 调查管理页面
    path('inv_manage/<int:investigation_id>/', views.inv_manage, name='inv_manage'),

    # 删除调查任务
    path('delete_inv/<int:investigation_id>/', views.delete_inv, name='delete_inv'),

    # 更改任务状态
    path('change_active/<int:investigation_id>/', views.change_active, name='change_active'),

    # 问卷调查页面
    path('do_paper/<str:school_year>/', views.do_paper, name='do_paper'),

    # 问卷管理页面
    path('paper_manage/<int:inv_id>/', views.paper_manage, name='paper_manage'),

    # 删除问卷
    path('delete_paper/<int:paper_id>/', views.delete_paper, name='delete_paper'),

    # 宿管老师列表页面
    path('teacher_list/<int:inv_id>/', views.teacher_list, name='teacher_list'),

    # 宿管老师统计结果页面
    path('teacher_result/<int:inv_id>/<int:teacher_id>/', views.teacher_result,
         name='teacher_result'),

    # 统计图表页面
    path('visual/<int:inv_id>/', views.visual, name='visual'),

    # 分班分寝主页
    path('sep_class/', views.sep_class, name='sep_class'),

    # 操作页
    path('sep_add/', views.sep_add, name='sep_add'),

    # 下载模板
    path('sep_temp/', views.sep_temp, name='sep_temp'),

    # 加入新生
    path('add_new', views.add_new_student, name='add_new_student'),

    # 下载错误文件
    path('download_error/<int:error_num>/', views.download_error, name='download_error'),

    # 入学年份选择页面
    path('sep_yl/', views.sep_yl, name='sep_yl'),

    # 查看页面
    path('sep_see/<int:grade_year>/', views.sep_see, name='sep_see'),

    # 删除单个新生
    path('sep_del/<int:student_id>/', views.sep_del, name='sep_del'),

    # 批量删除新生
    path('sep_del_year/<int:year>/', views.sep_del_year, name='sep_del_year'),

    # 修改新生信息
    path('sep_change_info/<int:student_id>/', views.sep_change_info, name='sep_change_info'),

    # 添加单个新生
    path('sep_add_one/<int:year>/', views.sep_add_one, name='sep_add_one'),

    # 按身份证号查询
    path('sep_que/', views.sep_que, name='sep_que'),

    # 导出某年新生
    path('sep_export/<int:year>/', views.sep_export, name='sep_export'),

    # 自定义时间段总结主页
    path('settable_summary', views.settable_summary, name='settable_summary'),

    # 自定义时间段详情页
    path('free_summary/<int:grade_num>/<str:date_area>/', views.free_summary, name='free_summary'),

    # 导出自定义时间段总结
    path('export_fs/<int:grade>/<str:start_date>/<int:total_days>/', views.export_fs,
         name='export_fs'),

    # 查看自定义时间段总结
    path('show_fs/<int:grade>/<str:start_date>/<int:total_days>/', views.show_fs,
         name='show_fs'),

    # 自定义时间段总结统计图表
    path('visual_fs/<int:grade>/<str:start_date>/<int:total_days>/', views.visual_fs,
         name='visual_fs'),

    # 自定义时间段总结班级统计图表
    path('visual_class/<str:gc_str>/<str:start_date>/<int:total_days>/', views.visual_class_fs,
         name='visual_class_fs'),

    # 用户管理页面
    path('user_manage/', views.user_manage, name='user_manage'),

    # 重置用户密码
    path('reset_pwd/<int:user_id>/', views.reset_pwd, name='reset_pwd'),

    # 标记/取消标记毕业
    path('change_graduated/<int:grade_year>/', views.change_graduated, name='change_graduated'),

    # 搬宿舍
    path('sep_change_dorm/<int:grade_year>/', views.sep_change_dorm, name='sep_change_dorm'),

    # 下载搬宿舍模板
    path('sep_cd_temp/<int:grade_year>/', views.sep_cd_temp, name='sep_cd_temp'),

    # 模板上传搬宿舍
    path('sep_cd/<int:grade_year>/', views.sep_cd, name='sep_cd'),

    # 宿舍管理权限分配
    path('dm_power/', views.dm_power, name='dm_power'),

    # 宿舍管理权限添加
    path('dmp_add/', views.dmp_add, name='dmp_add'),

    # 宿舍管理权限删除
    path('dmp_del/<str:dorm>/', views.dmp_del, name='dmp_del'),

    # 新增宿管老师
    path('add_teacher/', views.add_teacher, name='add_teacher'),

    # 删除宿管老师
    path('del_teacher/', views.del_teacher, name='del_teacher'),

    # 搬宿舍轨迹主页
    path('dm_lines_main/', views.dm_lines_main, name='dm_lines_main'),

    # 年份搬宿舍轨迹
    path('dm_lines/<int:year>/', views.dm_lines, name='dm_lines'),

    # 删除宿舍搬迁轨迹
    path('del_dm_line/<int:year>/<int:grade_index>/<str:od_key>/', views.del_dm_line, name='del_dm_line'),

    # 新增宿舍搬迁轨迹
    path('add_dm_line/<int:year>/', views.add_dm_line, name='add_dm_line'),

    # 查看请假离校情况
    path('see_leave/<int:err>/', views.see_leave, name='see_leave'),

    # 验证码管理
    path('captcha_manage/', views.captcha_manage, name='captcha_manage'),

    # 常用AI工具导航页
    path('my_ai/',views.my_ai, name='my_ai'),

    # 返校情况统计程序的url
    path('backtoschool/', include(('backtoschool.urls', 'backtoschool'),
                                  namespace='backtoschool')),

    # 班级卫生记分程序的url
    path('classclean/', include(('classclean.urls', 'classclean'),
                                namespace='classclean')),

    # 迟到记录系统的url
    path('late/', include(('late.urls', 'late'), namespace='late')),

    # 教师信息收集系统的url
    path('teachers/', include(('teachers.urls', 'teachers'), namespace='teachers')),

    # 车牌号信息收集系统的url
    path('cars_id/', include(('cars_id.urls', 'cars_id'), namespace='cars_id')),

    # 活动报名系统的url
    path('put_name/', include(('put_name.urls', 'put_name'), namespace='put_name')),

    # 两操长期假人员管理系统的url
    path('long_leave/', include(('long_leave.urls', 'long_leave'), namespace='long_leave')),

    # 社团信息管理系统的url
    path('club_info/', include(('club_info.urls', 'club_info'), namespace='club_info')),

    # 艺术节报名系统的url
    path('artday/', include(('artday.urls', 'artday'), namespace='artday')),

    # 工作量统计系统的url
    path('workload/', include(('workload.urls', 'workload'), namespace='workload')),

    # 银行卡号信息收集系统的url
    path('bank_id/', include(('bank_id.urls', 'bank_id'), namespace='bank_id')),

    # 运动会报名系统的url
    path('sport_meet/', include(('sport_meet.urls', 'sport_meet'), namespace='sport_meet')),

    # 中招美术加试报名系统的url
    path('zzbm/', include(('zzbm.urls', 'zzbm'), namespace='zzbm')),

    # 数学文化素材库的url
    path('math_culture/', include(('math_culture.urls', 'math_culture'), namespace='math_culture')),

    # 学生会管理系统的url
    path('su_manage/', include(('su_manage.urls', 'su_manage'), namespace='su_manage')),

    # 班会评价系统的url
    path('cm_eva/', include(('cm_eva.urls', 'cm_eva'), namespace='cm_eva')),

    # 课间操评价系统的url
    path('exercise_eva/', include(('exercise_eva.urls', 'exercise_eva'), namespace='exercise_eva')),

    # 期末评优评先上报系统的url
    path('praises/', include(('praises.urls', 'praises'), namespace='praises')),

    # 静态文件url
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
