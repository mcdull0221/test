import re
"""
re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
(re)	匹配括号内的表达式，也表示一个组
"""
a = 'python 11222java,666phpPythonPythonPythonPython2'

# r = re.findall('[a-z]{3,}', a)
r = re.findall('[a-z]{3,}?', a)   # 非贪婪模式
print(r)
s = re.findall('(Python){2}', a)
print(s)
