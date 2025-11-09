"""
    作者：郭雨健
    功能：统计当前项目代码总行数
    日期：2025.6.11
    版本：1.0
"""
import os


def main():
    """主函数"""
    # 计数变量
    lines_count = 0

    # 递归遍历整个目录树
    for dir_path, dl, fl in os.walk(os.getcwd()):
        for fn in fl:
            # 筛选出所有py和html文件
            if fn.split('.')[-1] in ['py', 'html']:
                # 合成文件路径
                fp = os.path.join(dir_path, fn)

                # 打开文件，读取行数
                try:
                    with open(fp, encoding='utf-8') as f:
                        total_lines = len(f.read().split('\n'))
                    lines_count += total_lines
                except UnicodeDecodeError:
                    # 不要了
                    pass

    # 输出总行数
    print('该项目代码总行数为{}'.format(lines_count))


if __name__ == '__main__':
    main()
