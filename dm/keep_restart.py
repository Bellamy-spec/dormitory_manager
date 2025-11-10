"""间隔一段时间重启服务器"""
import time
import sys
import os
from datetime import datetime


try:
    # 从命令行读取时间间隔
    t = int(sys.argv[1])
except IndexError:
    print('请设置时间间隔')
    sys.exit()

# 已执行次数
done = 0

while True:
    time.sleep(t)

    # 读取设置文件
    with open('dm/settings.py', 'r') as fi:
        settings_text = fi.read()

    # debug设置为False
    settings_text = settings_text.replace('DEBUG = True', 'DEBUG = False')

    # 学校名称设置
    with open('school_name.txt', encoding='utf-8') as fs:
        school_name = fs.read()
    settings_text = settings_text.replace('XX学校', school_name)

    # 获取设置文件行数
    rows = len(settings_text.split('\n'))

    # 删除旧文件，确保不会过写
    os.remove('dm/settings.py')

    # 重新写入设置文件
    with open('dm/settings.py', 'w') as fo:
        fo.write(settings_text)

    # 重启Apache2服务
    os.system('service apache2 restart')

    # 输出提示
    done += 1
    nt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    with open('output.txt', 'a') as f:
        f.write('完成第{}次重启，设置文件行数：{}  {}\n'.format(done, rows, nt))
