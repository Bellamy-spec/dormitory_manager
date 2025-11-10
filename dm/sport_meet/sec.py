"""生成班级口令"""
import random
from tools import DataTool
import pprint


# 实例化数据类
DT = DataTool()

# 初始化口令存放字典
pwd_dict = {}

for c in DT.get_class():
    # 生成六位随机密码
    pwd = ''
    for i in range(6):
        pwd += str(random.randint(0, 9))

    # 加入字典
    pwd_dict[c[0]] = pwd

# 写入
with open('sec.txt', 'w') as f:
    f.write(pprint.pformat(pwd_dict))
