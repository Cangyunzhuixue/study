# 覃晓
# 时间： 2022/4/16 0016 23:37
with open('logo.png','rb') as src_file:
    with open('copylogo2.png','wb') as target_file:
        target_file.write(src_file.read())