# 覃晓
# 时间： 2022/4/3 0003 17:19
''' 元组不可变序列，没有增删改查 '''
'''列表增删改查，对象地址没有变'''
'''列表式中括号，元组是小括号'''
lst = [10, 2, 30, 0]
print(id(lst))
lst.append(70)
print(lst)

'''创建方式'''
'''直接小括号'''
t = ('python', 'world', 2)
print(t)
print(id(t))
t2 = 'python', 'world', 2  # 小括号可以省略
print(t2)
t3 = ('Python')
print(t3, type(t3))  # 如果元组中只有一个元素，那么需要用小括号和逗号，否则认为是本身的数据类型
t4 = ('python',)
print(t4, type(t4))

'''内置函数创建'''
t1 = tuple(('Python', 'world', 98))
print(t1)
print(id(t1))

'''空元组，空列表，空字典创建'''
lst=[]
lst1=list()

d={}
d2=dict()

t5=()
t6=tuple()
