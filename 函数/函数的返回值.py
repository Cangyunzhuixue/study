# 覃晓
# 时间： 2022/4/13 0013 18:07
def fun(num):
    odd = []  # 存奇数
    even = []  # 存偶数
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even


lst = [12, 33, 45, 10.43, 22, 86]
print(fun(lst))
'''函数的返回值
一、如果没有返回值，可以不写return
二、如果返回的值为1个，直接返回类型
三、如果是多个，则返回元组
'''