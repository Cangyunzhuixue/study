# 覃晓
# 时间： 2022/4/3 0003 11:02
'''key的判断'''
scores = {'张三': 100, '李四': 200, '王五': 300}
print('张三' in scores)
print('张三' not in scores)

'''删除'''
del scores['张三']  # 删除指定键值对

scores.clear()  # 清空字典
print(scores)

scores['陈六'] = 100  # 新增
print(scores)

scores['陈六'] = 98  # 修改
print(scores)
