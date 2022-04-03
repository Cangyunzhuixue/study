# 覃晓
# 时间： 2022/4/3 0003 11:54
'''
内置函数zip()，将可迭代的对象作为参数，讲对象中的元素打包成一个元组
然后返回由这些元组组成的列表
'''
items = ['Fruit', 'Books', 'Other']
prices = [96, 78, 85]
lst = zip(items, prices)
print(list(lst))

d = {item: price for item, price in zip(items, prices)}
print(d)
