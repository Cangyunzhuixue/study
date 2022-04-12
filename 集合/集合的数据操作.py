# 覃晓
# 时间： 2022/4/13 0013 0:35

'''交集'''
s1={10,20,30,40}
s2={20,30,40,50,50,60}
print(s1.intersection(s2))
print(s1 & s2)

'''并集'''
print(s1.union(s2))
print(s1 | s2)

'''差集'''
print(s1.difference(s2))#减去交集那一部分
print(s1-s2)
print(s2.difference(s1))

'''对称差集'''
print(s1.symmetric_difference(s2))#并集减去交集那部分
print(s1 ^ s2)