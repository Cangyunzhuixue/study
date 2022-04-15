# 覃晓
# 时间： 2022/4/15 0015 20:54
# 覃晓
# 时间： 2022/4/15 0015 14:27
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值

cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 类有浅拷贝
print('---------------')
disk = Disk()
computer = Computer(cpu1, disk)
# 浅拷贝
import copy

computer2 = copy.deepcopy(computer)  # 复制的对象id和对象内的子对象id不一样
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)
