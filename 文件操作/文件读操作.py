# 覃晓
# 时间： 2022/4/16 0016 22:37
file = open('a.txt', 'r')
file.seek(2)
print(file.read())
print(file.tell())
file.close()