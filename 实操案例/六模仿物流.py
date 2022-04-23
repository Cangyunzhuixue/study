# 覃晓
# 时间： 2022/4/22 0022 23:42
lst = []
for i in range(0, 5):
    goods = input('输入编号和名称：')
    lst.append(goods)
for item in lst:
    print(item)
cart = []
while True:
    num = input('请输入商品编号：')


    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'q':
        break
print(cart)
