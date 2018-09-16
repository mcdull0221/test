# map 与匿名函数
li = [1,2,3,4,5]


def square(x):
    return x*x


r = map(square, li)
print(list(r))

r = map(lambda x: x*x, li)
print(list(r))
li_2 = [3,3,3,3,3,3,3,3,3]
r = map(lambda x, y: x*y, li, li_2)
print(list(r))
