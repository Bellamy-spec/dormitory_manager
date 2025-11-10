"""学生会管理系统的url模式"""
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

    # 第一步，设置学年
    path('change_step1/<int:school_year_id>/', views.change_step1, name='change_step1'),

    # 第二步，设置部门
    path('change_step2/<int:school_year_id>/', views.change_step2, name='change_step2'),

    # 停用部门
    path('deactivate_department/<int:department_id>/<int:school_year_id>/', views.deactivate_department,
         name='deactivate_department'),

    # 启用部门
    path('activate_department/<int:department_id>/<int:school_year_id>/', views.activate_department,
         name='activate_department'),

    # 修改部门
    path('change_department/<int:department_id>/<int:school_year_id>/', views.change_department,
         name='change_department'),

    # 第三步，加入成员
    path('change_step3/<int:school_year_id>/', views.change_step3, name='change_step3'),

    # 下载批量导入成员模板
    path('download_temp/', views.download_temp, name='download_temp'),

    # 下载错误文件
    path('download_error/<int:error_num>/', views.download_error, name='download_error'),

    # 查看某一届学生会成员列表
    path('member_list/<int:school_year_id>/<int:member_id>/', views.member_list, name='member_list'),

    # 获取当前学年
    path('get_current/', views.get_current, name='get_current'),

    # 往届学年列表页面
    path('school_year_list/', views.school_year_list, name='school_year_list'),

    # 完善部门介绍页面
    path('fbdp/', views.fbdp, name='fbdp'),

    # 提交部门介绍完善数据
    path('submit_fbdp/<department_id>/', views.submit_fbdp, name='submit_fbdp'),

    # 单个新增或修改成员
    path('edit_member/<int:school_year_id>/<int:member_id>/', views.edit_member, name='edit_member'),

    # 更新检查码
    path('up_member/<int:member_id>/', views.up_member, name='up_member'),

    # 删除成员
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),

    # 查看部门的页面
    path('see_department/', views.see_department, name='see_department'),

    # 部门管理页面
    path('dp_manage/', views.dp_manage, name='dp_manage'),

    # 删除部门
    path('delete_department/<int:department_id>/', views.delete_department, name='delete_department'),

    # 创建账号
    path('add_user/<int:member_id>/', views.add_user, name='add_user'),

    # 注销账号
    path('del_user/<int:member_id>/', views.del_user, name='del_user'),

    # 重置密码
    path('sp/<int:member_id>/', views.sp, name='sp'),

    # 导出检查码
    path('output_pwd/<int:school_year_id>/', views.output_pwd, name='output_pwd'),

    # 学年管理
    path('school_year_manage/', views.school_year_manage, name='school_year_manage'),

    # 修改学年
    path('edit_sy/<int:sy_id>/', views.edit_sy, name='edit_sy'),

    # 更改课间操检查工作人员
    path('config_worker/<int:sy_id>/', views.config_worker, name='config_worker'),

    # 下载更改课间操工作人员模板
    path('cw_temp', views.cw_temp, name='cw_temp'),
]
