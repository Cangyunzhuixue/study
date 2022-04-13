# 覃晓
# 时间： 2022/4/13 0013 23:07
'''斐波那契数列：1 1 2 3 5 8 。。。
n+1=n+(n-1)
'''


def fac(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fac(n - 1) + fac(n - 2)


for i in range(1, 11):
    print(fac(i), end='\t')
