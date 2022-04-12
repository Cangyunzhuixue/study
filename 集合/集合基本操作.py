# 覃晓
# 时间： 2022/4/12 0012 23:56
'''判断'''
s={10,20,30,40,50,856}
print(10 in s)
print(100 not in s)

'''新增'''
s.add(60)#添加一个
print(s)
s.update((40,88,22))#多个,
print(s)
s.update({11,77,33,23})
print(s)
s.update([90,'asd',98])
print(s)

'''删除'''
s.remove(10)#要求元素一定存在
print(s)
s.discard(500)#不要求一定存在
print(s)
s.pop()
print(s)#随机删除一个，没有参数
s.clear()#清空
print(s)