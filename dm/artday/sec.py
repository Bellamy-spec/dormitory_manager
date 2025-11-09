"""生成200个随机字符串并输出"""
import random
import pprint


def get_random_str():
    """生成一个长度为10的随机字符串"""
    # 初始化字符串
    random_str = ''

    # 可以包含的字符
    base_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    for i in range(10):
        random_str += base_str[random.randint(0, len(base_str) - 1)]

    return random_str


def main():
    """主函数"""
    # 初始化存放随机字符串的字典和列表
    sd, sl = {}, []

    # 初始id
    id_ = 1

    while id_ <= 200:
        # 生成随机字符串
        rs = get_random_str()

        # 过滤已存在的字符串
        if rs in sl:
            continue

        # 添加
        sd[rs] = id_
        sl.append(rs)

        # id加一
        id_ += 1

    # 格式化输出
    with open('sec.txt', 'w') as f:
        f.write(pprint.pformat(sd))
        f.write('\n')
        f.write(pprint.pformat(sl))


# call main()
if __name__ == '__main__':
    main()
