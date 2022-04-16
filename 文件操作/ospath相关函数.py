# 覃晓
# 时间： 2022/4/17 0017 0:20
import os.path

print(os.path.abspath('logo.png'))  # 返回绝对路径
print(os.path.exists('with语句.py'))  # 判断文件和目录是否存在
print(os.path.join('E\\Git', 'logo.png'))  # 目录和文件拼接
print(os.path.split('F:\\workplace\\study\\循环\\else.py'))  # 拆分目录和文件
print(os.path.splitext('logo.png'))  # 拆分文件名和后缀名
print(os.path.basename('flush与close.py'))  # 把文件名提取出来
print(os.path.dirname('F:\\workplace\\study\\循环\\else.py'))  # 提取目录，不提取文件名
print(os.path.isdir('F:\\workplace\\study\\循环\\else.py'))  # 判断是否目录
print(os.path.isdir('F:\\workplace\\study\\循环'))  # 判断是否目录
