"""批量创建zzbm系统操作员账号"""
# 导入用户前配置
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

from django.contrib.auth.models import User
import sys
from datetime import datetime
from zzbm.tools import DataTool

# 从命令行读取年份，若缺失默认为当前年份
try:
    year = sys.argv[1]
except IndexError:
    year = str(datetime.now().year)

# 实例化数据类，读取操作员数量
DT = DataTool()

# 添加用户
for i in range(1, DT.opes + 1):
    # 生成用户名
    username = str(year) + DT.str_two(i)

    # 创建用户
    user = User.objects.create_user(username=username)

    # 设置初始密码，保存
    user.set_password('106dycdyc')
    user.save()

print('成功创建{}个用户'.format(DT.opes))
