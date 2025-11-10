"""根据身份证号判断性别"""
# 导入用户前配置
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

from dm.scores.models import NewStudent, get_gender


for ob in NewStudent.objects.all():
    # 身份证号非空时执行判断
    if ob.id_number:
        ob.gender = get_gender(ob.id_number)
        ob.save()
