"""
    作者：郭雨健
    功能：生成当前项目源代码文档
    日期：2025.6.12
    版本：2.0
"""
import os
import pyperclip


def main():
    """主函数"""
    # 计数变量
    lines_str = ''

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
                        fs = f.read()
                except UnicodeDecodeError:
                    # 不要了
                    pass
                else:
                    # 加入代码文档
                    lines_str += '【' + fp + '】' + '\n'
                    lines_str += fs
                    lines_str += '\n' * 2

    # 存入剪贴板
    pyperclip.copy(lines_str)

    # 给出提示
    print('文档字符串已存至剪贴板')


if __name__ == '__main__':
    main()
