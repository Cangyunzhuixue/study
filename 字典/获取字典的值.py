# 覃晓
# 时间： 2022/4/3 0003 10:54
'''获取字典的值'''
scores = {'张三': 100, '李四': 200, '王五': 300}
'''d一 使用[]'''
print(scores['张三'])
# print(scores['陈留'])#如果值不存在，会报错
'''二’使用get()'''
print(scores.get('张三'))
print(scores.get('陈头岗刘'))  # 值不存在不报错
print(scores.get('麻六', 99))  # 99是查找麻六不存在的时候指定输出的默认值
