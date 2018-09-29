"""
闭包 = 函数 + 环境变量（函数定义时候）
不受外部环境变量影响，保存的是一个环境
"""


def curve_pre():
    a = 25
    b = 4

    def curve(x):
        print('this is curve')
        return a*b*x

    return curve


a = 10
f = curve_pre()
print(f(2))
print(f.__closure__)    # 闭包的环境变量
print(f.__closure__[0].cell_contents)   # 读出闭包的环境变量
