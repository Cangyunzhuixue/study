# 覃晓
# 时间： 2022/4/15 0015 21:57
'''将一个对象全部导入'''
import math

print(math.pi)

'''直接导入属性可以直接使用'''
from math import pi

print(pi)
'''导入自定义模块'''
import calc

print(calc.div(2, 3))
'''导入自定义模块中的某一函数'''
from calc import add

print(add(6, 8))
'''导入自定义模块中的某一函数且改名字'''
from calc import div as chu

print(chu(4, 2))
