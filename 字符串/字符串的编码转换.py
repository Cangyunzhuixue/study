# 覃晓
# 时间： 2022/4/13 0013 14:57
"""编码"""
s = '醉后不知天在水，满船清梦压星河'
print(s.encode(encoding='GBK'))  # 这个编码，一个中文两个字节
print(s.encode(encoding='UTF-8'))  # 一个中文三个字节

'''解码'''
byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte = s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
