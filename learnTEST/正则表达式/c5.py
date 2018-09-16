import re
"""
re*	匹配0个或多个的表达式。
re+	匹配1个或多个的表达式。
re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
"""
a = 'pytho1python1pythonn2'

r = re.findall('python?', a)

print(r)
