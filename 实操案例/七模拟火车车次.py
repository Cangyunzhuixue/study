# 覃晓
# 时间： 2022/4/23 0023 11:03
dict_ticket = {'G1569': ['北京-天津南', '18.05', '18:39', '00:34'],
               'G1568': ['北京-广州', '18.15', '18:40', '00:35'],
               'G1567': ['北京-上海', '18.26', '18:56', '00:30']
               }

print('车次\t\t出发站\t\t出发时间\t\t到达时间\t\t历时时长')
for item in dict_ticket:
    print(item, end=' ')  # 不换行
    for i in dict_ticket[item]:
        print(i, end='\t\t')
    print('')
'''输入要购买的车次'''
train_no = input('输入要购买的车次')
persons = input('输入乘车人，如果是多人，逗号隔开')
s = f'拟以购买了{train_no}车次'
s_info = dict_ticket[train_no]
s+=s_info[0]+' '+s_info[1]+'开'
