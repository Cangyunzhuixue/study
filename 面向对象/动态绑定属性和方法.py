# 覃晓
# 时间： 2022/4/14 0014 20:45
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print('-----stu2动态绑定性别属性-------')
stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)
print('----------------')
stu2.eat()
stu1.eat()


def show():
    print('定义在类之外，称函数')


stu1.show = show  # 绑定方法
stu1.show()
