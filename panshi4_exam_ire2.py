import re
from urllib.parse import unquote

# 磐石第四轮培训考试题目IRE2脚本

lines = []
with open(r'C:\Users\yibo\Desktop\access.log', 'r') as f:
    raw_lines = f.readlines()
    for i in raw_lines:
        if 'key2_is_here' in i:
            lines.append(i)
# print(lines)

new_lines = []
for j in lines:
    a = unquote(j.split(' ')[6])
    if '!=' in a:
        pattern = re.compile(r'!=[0-9]+')
        key = re.findall(pattern, a)[0]
        num_key = str(key).replace('!=', '')
        str_key = chr(int(num_key))
        print(str_key, end='')



