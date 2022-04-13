# 覃晓
# 时间： 2022/4/13 0013 14:39
'''%占位符'''
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))

'''{}占位符'''
print('我叫{0}，今年{1}岁'.format(name, age))

'''f-string'''
print(f'我叫{name},今年{age}岁')

'''宽度和精度'''
print('%10d' % 99)  # 10表示宽度
print('hhhhhhhhhh')
print('%.3f' % 3.1415926)  # 表示保留三位小数

'''同时表示宽度精度'''
print('%10.3f' % 3.1415926)

print('{0:.3}'.format(3.1415926))  # 表示三位数
print('{0:.3f}'.format(3.1415926))  # f表示三位数
print('{0:10.3f}'.format(3.1415926))  # f表示三位数,10表示宽度
