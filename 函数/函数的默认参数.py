# 覃晓
# 时间： 2022/4/13 0013 18:16
def fun(a, b=10):  # b就是默认值参数
    print(a, b)


fun(100)

fun(10, 100)  # 形参b将被赋值10
fun(10, b=34)  # 会形参b将被赋值10
print('hello', end='\t')  # end= 是print()的默认参数
print('world')

