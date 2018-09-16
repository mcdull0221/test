import time
# 带参数的装饰器
# 可接收任意数量参数的装饰器
# 可接收关键字参数的装饰器
# Python中，（*）会把接收到的参数形成一个元组，而（**）则会把接收到的参数存入一个字典


def runtime(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)

    return wrapper


@runtime
def f1(name):
    print('this is f1 '+name)


@runtime
def f2():
    print('this is f2 ')


@runtime
def f3(name1,name2, **kw):
    print('this is f2 '+name1+name2)
    print(kw)


f1('bob')
f2()
f3('ai', 'bub', a=1, b=2, c='22')
