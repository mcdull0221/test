
def f1():
    a = 0

    def f2():
        # a = 20    # 必须引用外部变量才能为闭包
        return a
    return f2


f = f1()
print(f)
print(f.__closure__[0].cell_contents)
