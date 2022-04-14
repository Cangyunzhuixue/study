# 覃晓
# 时间： 2022/4/14 0014 11:27
'''
打印错误信息
'''
import traceback

try:
    print(1 / 0)
except:
    traceback.print_exc()
