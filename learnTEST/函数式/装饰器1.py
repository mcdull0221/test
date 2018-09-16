import time
# 带参数的装饰器
# 可接收任意数量参数的装饰器


def runtime(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@runtime
def f1(name):
    print('this is f1 '+name)


@runtime
def f2():
    print('this is f2 ')


f1('bob')
f2()
