# 覃晓
# 时间： 2022/4/16 0016 19:33
file = open('b.txt', 'w', encoding='UTF-8')
file.write('hello，小明')  # 会覆盖
file2=open('c.txt','a')
file2.write('我爱你')
file.close()
