# 覃晓
# 时间： 2022/4/16 0016 23:14
'''
MyContentMgr实现了特殊方法__enter__和__exit__称该类对象遵守了上下文守则
实例对象称为上下文管理器
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被执行了')

    def show(self):
        print('show方法被执行了',1/0)


with MyContentMgr() as file:  # 相当于file=MyContentMgr()
    file.show()



