# 覃晓
# 时间： 2022/4/23 0023 12:16
'''enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。 '''
scores = (('广州', 72), ('北京国安', 70), ('上海上港', 66))
for index, item in enumerate(scores):#元组转换成带索引的两个
    print(index + 1, '.', end=' ')
    for score in item:
        print(score,end=' ')
    print( )


