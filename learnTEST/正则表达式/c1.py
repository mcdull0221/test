import re
a = '2Python6Java1C++3C#5C'

# print(a.index("python")>-1)
# print('python' in a)

r = re.findall('python', a)
print(r)
r1 = re.findall('\d', a)    # \d表示数字0-9
print(r1)
