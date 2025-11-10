"""测试用户与分组关系"""
from django.test import TestCase
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dm.settings')
django.setup()

from django.contrib.auth.models import User, Group


# Create your tests here.
def main():
    """主函数"""
    user = User.objects.get(id=1)
    print(user)


if __name__ == '__main__':
    main()
