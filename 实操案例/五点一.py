# 覃晓
# 时间： 2022/4/22 0022 23:11
'''猜数字'''
import  random
result = random.randint(1,100)
i = 0
while True:
    num = int(input('1-100内猜数字：'))
    if num > result:
        print('大了')
    elif num < result:
        print('小了')
    else:
        print('猜对了')
        break
    i += 1
print(f'猜了{i}次'.format(i))
