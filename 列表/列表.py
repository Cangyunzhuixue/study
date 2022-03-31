# 覃晓
# 时间： 2022/3/29 0029 17:12
'''第一种'''
lst = [1, 's']
'''第二种'''
lst2 = list(['hello', 'world'])
0
'''切片列表名[start，stop，步长]，默认步长1，默认起点1'''
lst1 = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst1[::2])
'''步长为负数'''
print(lst1[:2:-2])  # 切片的第一个元素默认是最后一个元素，从右边开始取数

print(lst1[5::-1])  # 切片的最后一个数默认是第一个元素，也是从右边开始取数
print('起点都是右边开始')
print(lst1[6:2:-2])  # 起点都是右边开始
print('''增加元素''')
lst.append('test')
print(lst)
print('删除元素')
lst1.append(30)
print(lst1)
lst1.remove(30)  # 只删除第一个元素
print(lst1)
lst1.pop(5)  # 移除对应索引的元素
print(lst1)
lst1.pop()
print(lst1)  # 不指定则删除最后一个
'''也可以用切片进行删除'''
print('原列表', lst1)
lst1[1:3] = []
print('新列表', lst1)
'''情空'''
lst1.clear()
print(lst1)
'''删除列表'''
del lst1
