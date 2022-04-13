# 覃晓
# 时间： 2022/4/13 0013 14:02
print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'))  # 获取字符原始值，即编码值
print(ord('杨'))
print(chr(97))  # 通过编码值找字符

'''===与is的区别
==B比较的是Value
is比较的是id是否相等'''
a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)

print(a is b)
print(b is c)
