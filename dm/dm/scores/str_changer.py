"""临时用来更改字符串的脚本"""


# 读取原字符串
with open('str_input.txt', encoding='utf-8') as fi:
    old_str = fi.read()

# 更改字符串
mid_str = old_str.replace('二', '三')
new_str = mid_str.replace('一', '二')

# 写入新字符串
with open('str_output.txt', 'w', encoding='utf-8') as fo:
    fo.write(new_str)
