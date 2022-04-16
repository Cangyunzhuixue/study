# 覃晓
# 时间： 2022/4/16 0016 19:39
src_file = open('logo.png', 'rb')
target_file = open('copyLogo.png', 'wb')
print(target_file.write(src_file.read()))
target_file.close()
src_file.close()
