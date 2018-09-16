from functools import reduce
# reduce
# 连续计算，连续的调用lambda

list_1 = [1,2,3,4,5,6,7,8]

r = reduce(lambda x,y: x+y ,list_1)     # 累加
print(r)

list_2 = ['a','b','v','d','g']
r = reduce(lambda x, y: x+y, list_2,'hi ')
print(r)


# map/reduce   编程模型,映射 规约   并行计算
