# 覃晓
# 时间： 2022/4/13 0013 12:06
'''判断字符串是否是合法的标识符'''
s = 'hello,python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())

'''判断是否全部是空格'''
print('4.', '\t'.isspace())

'''判断是否全部字母'''
print('5.', 'acb'.isalpha())
print('6.', '张三'.isalpha())  # 汉字也是字母
print('7.', '张三1'.isalpha())

'''判断是否全部是十进制数'''
print('8.', '123214'.isdecimal())
print('9.', '123214四'.isdecimal())
print('10.', 'ⅠⅡⅢⅣ'.isdecimal())

'''判断是否全部是数字'''
print('11.', '123214四'.isnumeric())  # 中文数字也是数字
print('12.', 'ⅠⅡⅢⅣ'.isnumeric())  # 罗马数字也是数字

'''判断是否全部是数字字母'''
print('13.', '四三二一ⅠⅡⅢⅣ12334q请问'.isalnum())
