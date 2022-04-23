# 覃晓
# 时间： 2022/4/22 0022 17:35
import os

filename = 'test.txt'
'''向文件中输出’奋斗成就更好的呢‘'''
with open(filename, 'w', encoding='utf-8') as wFile1:
    wFile1.write('奋斗成就更好的你')
fp = open('test1.txt', 'w', encoding='utf-8')
print('奋斗成就更好的我', file=fp)
fp.close()
