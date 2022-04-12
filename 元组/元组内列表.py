# 覃晓
# 时间： 2022/4/12 0012 22:41
t=(10,[20,30],7)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

'''尝试修改'''
#t[1]=100不可以修改元组内荣，但是可以修改元组内列表内容

t[1].append(45)
print(t[1][1])
t[1][2] = 'python'
print(t[1])


