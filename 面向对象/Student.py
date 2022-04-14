# 覃晓
# 时间： 2022/4/14 0014 20:10
class Student:  # 类名一个或多个单词组成，每个单词首字母大写，其他的小写
    native_pace = '吉林'  # 直接写在类里边的变量，叫作雷属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print('在吃饭')

    # 静态方法
    @staticmethod
    def mothod():
        print('使用了@staticmethod，所以是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('使用了@classmethod，所以是类方法')


# 类之外定义的叫函数，在类里边的叫方法
def drink():
    print('喝水')


# 创建Student的对象
stu1 = Student('张三', 20)
stu2 = Student('李四', 21)
'''调用类方法'''
# stu1.eat()
# Student.eat(stu1)  # 功能跟stu1.eat()相同
'''调用类属性'''
# print(Student.native_pace)
# print(stu1.native_pace)
# print(stu2.native_pace)
# stu1.native_pace = '长春'
# print(stu1.native_pace)
# print(stu2.native_pace)
'''类方法'''
# Student.cm()
'''静态方法方法'''
# Student.mothod()
'''创建的类也是一个对象
print(id(Student))
print(type(Student))
print(Student)
'''
