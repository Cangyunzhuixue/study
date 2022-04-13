# 覃晓
# 时间： 2022/4/13 0013 14:14
s = 'hello,Python'
s1 = s[:5]  # 没有指定起始位置。默认从0开始
s2 = s[6:]  # 没有指定结束位置。默认到最后开始
print(s1)
print(s2)
s3 = '!'
newStr = s1 + s3 + s2
print(newStr)

print('-------切片start:end:step--------')
print(s[1:5:1])  # 从1开始截，直到5（不包括5）
print(s[::2])  # 两个元素索引间隔为2
print(s[::-2])  # 默认从字符串最后一个开始，第一个结束
print(s[-6:])
