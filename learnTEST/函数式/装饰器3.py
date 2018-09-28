import time
from functools import reduce


def performance(f):
    def runtime(*args, **kw):
        t1 = time.time()
        print('t1 '+str(t1))
        r = f(*args, **kw)
        t2 = time.time()
        print('t2 '+str(t2))
        t = t2 - t1
        print(t)
        return r    # 返回factorial函数的执行
    return runtime


@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))


print(factorial(4))
