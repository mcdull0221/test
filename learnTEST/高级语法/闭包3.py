x = 0


def f1():
    pos = 0

    def f2(x1):
        nonlocal pos
        new_pos = pos + x1
        pos = new_pos
        return new_pos

    return f2


f = f1()
print(f(1))
print(f(1))
print(f(1))
