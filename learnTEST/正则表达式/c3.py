import re

"""
\w	匹配字母数字及下划线
\W	匹配非字母数字及下划线
\s	匹配任意空白字符，等价于 [\t\n\r\f].
\S	匹配任意非空字符
\d	匹配任意数字，等价于 [0-9].
\D	匹配任意非数字
"""
a = '1239pyt,ho n08_2java5yj&*\n/'
print('adr\radf')
r = re.findall('\W', a)
print(r)


