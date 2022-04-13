# 覃晓
# 时间： 2022/4/13 0013 13:28
'''替换操作'''
s = 'hellp,Python'
print(s.replace('Python', 'Java'))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python', 'Java', 2))

'''连接操作，将列表或者元组中的字符串合并成一个字符'''
lst = ['hello','Java','Python']
print('|'.join(lst))
print(''.join(lst))

t= ['hello', 'Java', 'Python']
print(''.join(t))
print('  '.join(t))
print('a'.join('b'))