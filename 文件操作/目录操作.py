# 覃晓
# 时间： 2022/4/16 0016 23:48
# os模块是与操作系统相关的一个模块
import os

# os.system('calc.exe')
# 可以直接调用可执行文件
# os.startfile('E:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe')
# 返回当前工作目录
print(os.getcwd())
print(os.listdir('../文件操作'))

os.rmdir('test')
