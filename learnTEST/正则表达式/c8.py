import re
"""
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
"""
s = 'life is short, i use python'

r = re.findall('life(.*)python', s)
a = re.search('life(.*)python', s)
print(r)
print(a.group(0))
