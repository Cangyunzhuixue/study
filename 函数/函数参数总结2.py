# 覃晓
# 时间： 2022/4/13 0013 20:19
def fun(a, b=10):  # b是默认值形参
    print('a=', a)
    print('b=', b)


def fun2(*args):  # 个数可变位置的形参
    print(args)


def fun3(**args2):  # 个数可变的关键字形参
    print(args2)


fun2(1, 0, 2, 34, 2)
fun3(a=11, b=88, c=99, d=23)


def fun4(a, b, *c, d):  # 从这*之后只能采用关键字传参
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


# fun4(10, 4, 3, 5)  # 位置实参传递
fun4(a=10, b=4, c=5, d=9)  # 关键字实参传递
fun4(4, 5, c=2, d=5)  # 前两个位置，后两个关键字

'''函数定义时的形参顺序问题'''


def fun5(a, b, *, c, d, **args):
    pass


def fun6(*args, **args2):
    pass


def fun7(a,b,*args,**args2):
    pass
