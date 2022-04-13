# 覃晓
# 时间： 2022/3/29 0029 11:03
for i in range(100,1000):
    a=i%10
    b=i//10%10
    c=i//100
    if a**3+b**3+c**3==i:
        print(i)
    pass