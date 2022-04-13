# 覃晓
# 时间： 2022/4/13 0013 11:26
s = 'hello,python'
print(s.center(20, '*'))  # 居中

print(s.ljust(20, "*"))  # 左对齐

print(s.ljust(10))  # 位置过小，返回原字符

print(s.rjust(20,'*'))#右对齐
print(s.rjust(20))#默认空格填充

print(s.zfill(20))#右对齐，0填充
print('-7872'.zfill(10))