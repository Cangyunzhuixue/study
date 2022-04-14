# 覃晓
# 时间： 2022/4/14 0014 23:13
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = C('Samuro', 20)
print(x.__dict__)  # 返回对象或者实例的属性的字典
print(C.__dict__)
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出父类的元组
print(C.__base__)  # 输出跟其最近的父类
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 查看子类
