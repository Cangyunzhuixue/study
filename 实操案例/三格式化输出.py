# 覃晓
# 时间： 2022/4/22 0022 19:49
def fun():
    num = int(input('输入一个十进制的整数:'))
    print(num, '的二进制数为：', bin(num))  # 二进制
    print(str(num) + 'de 二进制数为：' + bin(num))  # 字符串连接
    print('%s的二进制数为：%s' % (num, bin(num)))  # 格式化字符串
    print('{0}的二进制数为：{1}'.format(num, bin(num)))  # 格式化字符串
    print(f'{num}的二进制数是:{bin(num)}')
    print('==========================')
    print(f'{num}的八进制为：{oct(num)}')
    print(f'{num}的十六进制数为：{hex(num)}')


if __name__ == '__main__':
    try:
        fun()
    except:
        print('只能输入整数')
        fun()
