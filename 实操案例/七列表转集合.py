# 覃晓
# 时间： 2022/4/22 0022 23:58
name = ['张三', '李四', '王五', '老六']
sex = ['男', '女', '男', '女']
a = dict(zip(name, sex))
for item in a:
    print(item, a[item])
print('============================')
b = zip(name, sex)  # 转成集合
print(type(b))
c = dict(b)  # 转换成字典
print(type(c))
print(c)
for item in c:
    print(item)
