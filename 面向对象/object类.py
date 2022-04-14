# 覃晓
# 时间： 2022/4/14 0014 22:52
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


'''重写__str___'''


def __str__(self):
    return '我的名字是{0}，今年{1}岁'.format(self.name, self.age)


pass

stu = Student('张三', 20)
print(dir(stu))  # 返回对象所有属性
print(stu)  # 重写的str
