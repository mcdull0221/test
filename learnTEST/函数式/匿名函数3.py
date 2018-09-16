# filter 过滤掉False

list_1 = [1,0,0,1,0,1,0,1,1,0]
r = filter(lambda x: True if x ==1 else False, list_1)
print(list(r))
