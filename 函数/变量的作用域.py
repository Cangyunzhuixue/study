# 覃晓
# 时间： 2022/4/13 0013 21:47
def fun(a, b):
    c = a + b  # abc是局部变量，只在函数内有效
    print(c)


name = '覃sir'  # name是全局变量，在函数内外都可以使用
print(name)


def fun2():
    print(name)
    pass


fun2()


def fun3():
    global age  # 函数内不定义的变量，局部变量使用global，这个变量就是全局变量
    age = 30
    print(age)


fun3()
print(age)
