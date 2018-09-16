
def f1():
    a = 10

    def f2():
        #   此时a将会被认为局部变量
        a = 20
        print("第一个" + str(a))
    print("第二个" + str(a))
    f2()
    print("第三个" + str(a))


f1()
