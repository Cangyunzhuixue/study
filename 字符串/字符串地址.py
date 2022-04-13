# 覃晓
# 时间： 2022/4/13 0013 10:12
'''字符串内存地址只有一份'''
a='a'
b="a"
c='''a'''
print(a,id(a))
print(b,id(b))
print(c,id(c))