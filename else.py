# 覃晓
# 时间： 2022/3/29 0029 16:39
'''如果不执行循环中的break，就会与外边的else配对'''
for i in range(3):
    pwd = input('输入密码：')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起，三次密码都错误')
'''while'''
a = 0
while a < 3:
    pwd = input('输入密码')
    if pwd == '888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
else:
    print('对不起，三次密码都错误')
