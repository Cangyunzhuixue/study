# 覃晓
# 时间： 2022/4/14 0014 21:51
class Person(object):  # Person默认继承object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):  # 在括号里边上多个父类命表示继承
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear


stu = Student('张三', 20, '123')
teacher = Teacher('李四', 34, 10)
stu.info()
teacher.info()
