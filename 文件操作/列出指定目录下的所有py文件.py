# 覃晓
# 时间： 2022/4/17 0017 0:52
# 列出指定目录下的所有py文件
import os
'''
import os.path

path = os.getcwd()
lst = os.listdir(path)
for fileAndDir in lst:
    if os.path.isdir(fileAndDir):
        continue
    else:
        set1 = os.path.splitext(fileAndDir)
        if set1[1] == '.py':
            print(fileAndDir)
'''
import os.path

path = os.getcwd()
lst = os.listdir(path)
for fileAndDir in lst:
    if fileAndDir.endswith('.py'):
        print(fileAndDir)