# 覃晓
# 时间： 2022/4/13 0013 17:21
def calc(a, b):  # 形参
    c = a + b
    return c


def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)


result = calc(10, 20)  # 实参
print(result)

n1 = 11
n2 = [22, 33, 44, 55]
fun(n1, n2)

'''函数的返回值'''
