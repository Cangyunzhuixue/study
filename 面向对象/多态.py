# 覃晓
# 时间： 2022/4/14 0014 23:01
'''多态就是多种形态，它是指：即便不知道一个变量所引用的额对象是什么类型，仍然可以通过这个变量调用方法，
在运行过程中根军变量所引用对象的类型，动态地决定调用哪个对象中的方法'''


class Animal(object):
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
