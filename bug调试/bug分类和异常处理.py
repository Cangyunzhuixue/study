# 覃晓
# 时间： 2022/4/14 0014 9:50
'''常见bug'''
'''越界'''
lst = [1, 2, 3, 4]
# print(lst[5])#访问越界

# lst.append('A', 'B')  # 方法参数不不对

'''输入两个整数，除法'''
'''
while True:
    try:
        a = int(input('第一个整数：'))
        b = int(input('第二个整数：'))
        result = a / b  # 当除数是0或者输入特殊字符会报错
        print(result)
        break
    except ZeroDivisionError:
        print('除数不可以为零')
    except ValueError:
        print('请输入整数')
    except BaseException:
        print('重新输入')
'''
'''try-except-else 抛出异常执行except后边内容，否则执行else后边内容'''

'''
try:
    a = int(input('第一个整数：'))
    b = int(input('第二个整数：'))
    result = a / b  # 当除数是0或者输入特殊字符会报错
except BaseException as e:
    print('出错了', e)
else:
    print('计算结果是：', result)
'''

'''try-except-else-finally 抛出异常执行except后边内容，否则执行else后边内容,finally无论如何都会执行的
常用来释放try申请的资源
'''
try:
    a = int(input('第一个整数：'))
    b = int(input('第二个整数：'))
    result = a / b  # 当除数是0或者输入特殊字符会报错
except BaseException as e:
    print('出错了', e)
else:
    print('计算结果是：', result)
finally:
    print('程序结束')
