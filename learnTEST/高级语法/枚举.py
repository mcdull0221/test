from enum import Enum,unique
# 枚举意义 重在于标签
"""
1 定义枚举时，成员名称不允许重复　
2 默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名　　
如果想把值重复的成员也遍历出来，要用枚举的一个特殊属性__members__
3 如果枚举中存在相同值的成员，在通过值获取枚举成员时，只能获取到第一个成员
4 如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
5 枚举中的值不允许修改

"""
class Color(Enum):
    RED = 1
    GREEN = 2
    BLACK = 3
    YELLOW = 4
    RED_ALIAS = 1


@unique
class Color1(Enum):
    RED = 1
    GREEN = 2
    BLACK = 3
    YELLOW = 4


# for color in Color.__members__:
for color in Color:
    print(color)

print(Color.BLACK)
print(Color.RED is Color.RED)
print(Color.BLACK == Color.RED)
print(Color.GREEN == 2)
print(Color.RED is Color1.RED)

a = 1
print(Color(a))
