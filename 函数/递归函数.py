# 覃晓
# 时间： 2022/4/13 0013 22:19
'''递归实现阶乘'''


def fun(n):
    if n == 1:
        return 1
    else:
        return n * fun(n - 1)


print(fun(6))
