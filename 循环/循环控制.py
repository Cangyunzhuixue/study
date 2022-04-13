# 覃晓
# 时间： 2022/3/29 0029 11:20
# break直接退出循环
# for i  in range(3):
#     pwd=input('输入密码')
#     if pwd=='888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
# 结束当前训话 ，进入下一次循环
'''输出1到50的5的倍数'''
# for i in range(1, 51):
#     if i % 5 == 0:
#         print(i)
'''使用continue'''
for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)
