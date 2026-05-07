"""脚本：动态生成考试时间选项并存入json"""
# 导入用户前配置
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

import json
from zzbm.tools import DataTool
from zzbm.models import Task
from datetime import datetime
from django.utils import timezone

# 实例化静态数据类
DT = DataTool()


def main():
    """主函数"""
    # 锁定当前年份与任务对象
    current_year = str(datetime.now().year)
    exam_time_dict = {}

    try:
        task = Task.objects.filter(year=current_year)[0]
    except IndexError:
        # 当前年份无任务，不会出现这种情况，返回空对象即可
        pass
    else:
        # 开始操作
        if task.exam_time_active:
            if timezone.now() < task.start_time_ob:
                exam_time_dict['0'] = DT.show_sted(task.start_time, task.format_start_time)
        if task.exam_time_active_1:
            if timezone.now() < task.start_time_ob_1:
                exam_time_dict['1'] = DT.show_sted(task.start_time_1, task.format_start_time_1)
        if task.exam_time_active_2:
            if timezone.now() < task.start_time_ob_2:
                exam_time_dict['2'] = DT.show_sted(task.start_time_2, task.format_start_time_2)
        if task.exam_time_active_3:
            if timezone.now() < task.start_time_ob_3:
                exam_time_dict['3'] = DT.show_sted(task.start_time_3, task.format_start_time_3)
        if task.exam_time_active_4:
            if timezone.now() < task.start_time_ob_4:
                exam_time_dict['4'] = DT.show_sted(task.start_time_4, task.format_start_time_4)
        if task.exam_time_active_5:
            if timezone.now() < task.start_time_ob_5:
                exam_time_dict['5'] = DT.show_sted(task.start_time_5, task.format_start_time_5)

    # 对象存入json文本
    with open('exam_time.json', 'w') as f:
        f.write(json.dumps(exam_time_dict, ensure_ascii=False))


if __name__ == '__main__':
    main()
