# 覃晓
# 时间： 2022/4/13 0013 11:15
'''字符串中的大小写转换方法'''
'''转换之后会产生新的字符串，即使全部小写，转换小写也会产生新的字符串'''
s='hello,python'
print(s,id(s))
a=s.upper()
b=s.lower()
print(a,id(a))
print(b,id(b))

s2='HeLLo ,pythoN'
print(s2.swapcase())
print(s2.capitalize())
print(s.title())