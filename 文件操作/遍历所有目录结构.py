# 覃晓
# 时间： 2022/4/17 0017 1:08
import os

path = os.getcwd()
lst_files = os.walk(path)  # 返回元组,元组内是路径名，包含的路径名，文件名
for dirpath, dirname, filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    for dir in dirname:
        print(os.path.join(dirpath,dir))
