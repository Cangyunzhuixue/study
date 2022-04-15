# 覃晓
# 时间： 2022/4/15 0015 12:02
class Person(object):
    # __new__负责创建对象，讲创建的对象返回__init__进行初始化
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的ID为{0}'.format(id(obj)))
        return obj  # 返回值传到__init__的self

    # 从New获取了obj进行对象的初始化
    def __init__(self, name, age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id是{0}'.format(id(object)))
print('Person这个类对象的id是{0}'.format(id(Person)))

per = Person('张三', 20)
# print(per)
