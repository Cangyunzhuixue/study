# 覃晓
# 时间： 2022/4/3 0003 11:17
scores = {'张三': 100, '李四': 200, '王五': 300}

'''获取所有key'''
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有的key组成的试图转成列表
print('-----分割线-----')

# 获取所有的value
values = scores.values()
print(values)
print(type(values))
print(list(values))

# 获取所有的key-value对
items = scores.items()
print(items)
print(list(items))  # 转换之后的列表元素是元组组成
