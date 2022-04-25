# 覃晓
# 时间： 2022/4/23 0023 19:52
def calc(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        if b != 0:
            return div(a, b)
        else:
            print('除数不能为零')


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    op = input('输入运算符：')
    print(calc(a, b, op))
