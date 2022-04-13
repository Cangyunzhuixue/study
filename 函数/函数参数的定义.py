# 覃晓
# 时间： 2022/4/13 0013 18:31
def fun(*args):  # 无法确定实参个数
    print(args)  # 结果是元组
    print(args[0])


fun(10)
fun(10, 20)
fun(10, 20, 30)


def fun1(**args):
    print(args)  # 返回字典


fun1(a=10)
fun1(a=10, b=20, c=30)
