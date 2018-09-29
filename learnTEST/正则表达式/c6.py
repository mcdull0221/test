import re
"""匹配边界
^	匹配字符串的开头
$	匹配字符串的末尾。
"""
a = '100000000'

r = re.findall('^\d{3,8}$', a)

print(r)
