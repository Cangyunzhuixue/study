# 覃晓
# 时间： 2022/4/22 0022 20:19
pwd = input('字符包支付密码：')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，只能是数据')
print('==============================')
s = '支付数据合法' if pwd.isdigit() else '支付数字不合法，只能是数据'
print(s)
a = 3 if 4 < 5 else 7
print(a)
