# 覃晓
# 时间： 2022/4/14 0014 22:15
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def run(self):
        print('===走路===')


class Chinese(Person):
    def __init__(self, name, gender, age, china_id):
        super().__init__(name, gender, age)
        self.china_id = china_id

    def say(self):
        print('===你好===')


class Student:
    def __init__(self, sno, stu_class):
        self.sno = sno
        self.stu_class = stu_class

    def study(self):
        print('===在学习===')


'''多继承进行初始化'''


class ChineseStudent(Chinese, Student):
    def __init__(self, name, gender, age, china_id, sno, stu_class):
        Chinese.__init__(self, name, gender, age, china_id)
        Student.__init__(self, sno, stu_class)


if __name__ == '__main__':
    zhangSan = ChineseStudent("张三", "男", "24", "342623199810234589", "2111908923", "计算机1班")
    print(zhangSan.name)  # 调用Person的属性
    zhangSan.run()  # 调用Person的方法
    print("身份证号码：", zhangSan.china_id)  # 调用Chinese属性
    zhangSan.say()  # 调用Chinese方法
    print(zhangSan.stu_class)  # 调用Student属性
    zhangSan.study()  # 调用Student方法
