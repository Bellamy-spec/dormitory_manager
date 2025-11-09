"""中招美术加试报名系统的url模式"""
from django.urls import path
from . import views


urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 登录页面
    path('login/', views.login1, name='login'),

    # 注销登录
    path('logout/', views.logout_view, name='logout'),

    # 设置密码
    path('setpassword/', views.set_pwd, name='set_pwd'),

    # 年份列表
    path('year_list/', views.year_list, name='year_list'),

    # 任务主页
    path('task_main/<int:task_id>/', views.task_main, name='task_main'),

    # 发布任务
    path('public/', views.public, name='public'),

    # 删除任务
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

    # 任务管理页
    path('task_manage/<int:task_id>/', views.task_manage, name='task_manage'),

    # 更改截止日期
    path('change_date/<int:task_id>/', views.change_date, name='change_date'),

    # 更改任务状态
    path('change_active/<int:task_id>/', views.change_active, name='change_active'),

    # 列出已报名考生
    path('list_put/<int:task_id>/<int:st_id>/', views.list_put, name='list_put'),

    # 考生报名
    path('put_name/<int:task_id>/', views.put_name, name='put_name'),

    # 查询页
    path('que/<int:task_id>/', views.que, name='que'),

    # 考生查看页
    path('student/<int:student_id>/<str:pwd>/', views.stu, name='student'),

    # 删除已报名考生
    path('delete_st/<int:student_id>/<int:delete_method>/', views.delete_st, name='delete_st'),

    # 设置考场人数
    path('set_len/<int:task_id>/', views.set_len, name='set_len'),

    # 设置考试时间
    path('set_time/<int:task_id>/', views.set_time, name='set_time'),

    # 开放/关闭准考证下载
    path('change_open/<int:task_id>/', views.change_open, name='change_open'),

    # 在线生成、下载准考证
    path('download_card/<int:student_id>/<str:pwd>/', views.download_card, name='download_card'),

    # 在线生成、下载考场座次表
    path('get_seat_table/<int:task_id>/', views.get_seat_table, name='get_seat_table'),

    # 导出考生信息
    path('export_students/<int:task_id>/', views.export_students, name='export_students'),

    # 成绩管理主页
    path('score_manage/<int:task_id>/', views.score_manage, name='score_manage'),

    # 查成绩链接
    path('student_score/<int:student_id>/<str:pwd>/', views.get_score, name='get_score'),

    # 下载成绩模板
    path('download_temp/<int:task_id>/', views.download_temp, name='download_temp'),

    # 上传成绩
    path('write_score/<int:task_id>/', views.write_score, name='write_score'),

    # 下载错误文件
    path('download_error/<int:error_num>/', views.download_error, name='download_error'),

    # 打开/关闭自动分配考场、考号
    path('change_give/<int:task_id>/', views.change_give, name='change_give'),

    # 找回报名序号页面
    path('find_pwd/<int:task_id>/', views.find_pwd, name='find_pwd'),

    # 批量导入考生主页
    path('multi_export/<int:task_id>/', views.multi_export, name='multi_export'),

    # 下载批量导入考生的模板
    path('multi_temp/', views.multi_temp, name='multi_temp'),

    # 模板批量导入考生
    path('write_students/<int:task_id>/', views.write_students, name='write_students'),

    # 直接查询成绩的页面
    path('get_score_input/<int:task_id>/', views.get_score_input, name='get_score_input'),

    # 核对信息验证
    path('get_in/<int:task_id>/', views.get_in, name='get_in'),

    # 核对信息
    path('check/<int:student_id>/', views.check, name='check'),

    # 完善身份证号
    path('complete_id/<int:student_id>/', views.complete_id, name='complete_id'),

    # 查看批量导入的考生
    path('see_students/<int:task_id>/', views.see_multi, name='see_multi'),

    # 修改已导入考生的信息
    path('change_info/<int:student_id>/', views.change_info, name='change_info'),

    # 重设考场分配参数
    path('reset_task_num/<int:task_id>/', views.reset_task_num, name='reset_task_num'),

    # 修改考生信息
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),

    # 标记或取消标记缺考
    path('change_miss/<int:student_id>/', views.change_miss, name='change_miss'),

    # 导出成绩单
    path('export_score/<int:task_id>/<int:pub>/', views.export_score, name='export_score'),

    # 导出无成绩考生
    path('none_score/<int:task_id>/', views.none_score, name='none_score'),

    # 导出去重成绩单
    path('de_repeat/<int:task_id>/<int:pub>/', views.de_repeat, name='de_repeat'),

    # 导出重复考生
    path('show_repeat/<int:task_id>/', views.show_repeat, name='show_repeat'),

    # 查成绩开关
    path('que_ctrl/<int:task_id>/', views.que_ctrl, name='que_ctrl'),

    # 已结束的场次数
    path('change_start_turn/<int:task_id>/<int:target>/', views.change_start_turn, name='change_start_turn'),

    # 登记缺考考场选择
    path('load_miss_main/', views.load_miss_main, name='load_miss_main'),

    # 考务工作人员标记或取消标记缺考
    path('change_miss_1/<int:student_id>/', views.change_miss_1, name='change_miss_1'),

    # 考场密码管理
    path('room_pwd_manage/<int:task_id>/', views.room_pwd_manage, name='room_pwd_manage'),

    # 考场密码更新
    path('room_pwd_update/<int:task_id>/', views.room_pwd_update, name='room_pwd_update'),
]
