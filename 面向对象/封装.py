# 覃晓
# 时间： 2022/4/14 0014 21:25
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('启动了')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 不希望外部使用，所以加了两个__

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()
# print(stu.__age)  # 无法访问
print(dir(stu))
print(stu._Student__age)  # 这种形式可以访问，但是不建议
print()
