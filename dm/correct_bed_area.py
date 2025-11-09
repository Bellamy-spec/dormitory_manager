"""修正床铺信息"""
# 导入用户前配置
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

from dm.scores import models, data


# 实例化静态数据类
DT = data.Data()

obs = models.Record.objects.all()
n = len(obs)

for i in range(n):
    ob = obs[i]
    ob.bed_area = dict(DT.ap)[ob.bed]
    ob.save()

    # 显示完成率
    print('\033[F\033[K', end='')
    print('已完成{}/{}'.format(i + 1, n))
