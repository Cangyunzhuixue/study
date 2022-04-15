# 覃晓
# 时间： 2022/4/14 0014 23:43
a = 20
b = 100
c = a + b
d = a.__add__(b)  # 相加
print(d)


class Student:
    def __init__(self, name):
        self.name = name


'''__add__'''


def __add__(self, other):
    return self.name + other.name


'''__len___'''


def __len__(self):
    return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2  # __add__实现两个对象的加法运算
print(s)
print('-----------------------')
lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
# 输出对象的长度，需要添加__len__
print(len(stu1))
