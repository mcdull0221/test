import time


def runtime(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@runtime
def f1():
    print('this is f1')


@runtime
def f2():
    print('this is f2')


f1()
f2()
