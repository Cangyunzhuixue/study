# 覃晓
# 时间： 2022/4/22 0022 23:26
year = [12, 55, 78, 99, 00, 44, 11, 00]
print(year)
for index, value in enumerate(year):  # 这个函数产生列表的索引和对应的值
    if str(value) != '0':
        year[index] = int(str('19' + str(value)))
    else:
        year[index] = 2000
print(year)
