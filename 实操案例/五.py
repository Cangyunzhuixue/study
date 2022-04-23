# 覃晓
# 时间： 2022/4/22 0022 22:29
'''循环输出26个字符对应的ascll'''
# al_list = [chr(i) for i in range(97, 123)]
# print(al_list)

# x = 97
# for _ in range(1, 27):  # 只需要循环次数，不需要迭代，可以用_
#     print(chr(x), '-->', x)
#     x += 1

for i in range(1, 4):
    accout = input('请输入账户名')
    pwd = input('请输入密码')
    if pwd == '888' and accout == 'admin':
        print('登录成功')
        break
    elif i == 3:
        print('三次输入都错误')
    else:
        print(f'用户名或者密码错误，还有{3 - i}次机会'.format(3 - i))
print('=========================')
for i in range(1, 4):
    accout = input('请输入账户名')
    pwd = input('请输入密码')
    if pwd == '888' and accout == 'admin':
        print('登录成功')
        break
    else:
        print('用户名或者密码错误')
        if i < 3:
            print(f'还有{3 - i}次机会'.format(3 - i))
else:  # for正常退出，执行这个else
    print('三次输入都错误')
