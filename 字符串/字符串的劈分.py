# 覃晓
# 时间： 2022/4/13 0013 11:56
'''split()从左侧劈分'''
s = 'hello word python'
lst = s.split()  # 默认分隔符是空格
print(lst)

s1 = 'hello|world|python'
print(s1.split(sep='|'))  # 指定分割符
print(s1.split(sep='|', maxsplit=1))  # 指定分割符合分割次数

'''rsplit()从右侧开始劈分'''
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep='|',maxsplit=1))

