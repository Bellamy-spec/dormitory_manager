"""测试用户与分组关系"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

from django.contrib.auth.models import User, Group


def main():
    """主函数"""
    user = User.objects.get(id=1)
    group = Group.objects.get(name='Student')
    # user.groups.add(group)
    # user.groups.remove(group)
    print(group in user.groups.all())


if __name__ == '__main__':
    main()
