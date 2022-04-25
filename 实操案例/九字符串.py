# 覃晓
# 时间： 2022/4/23 0023 18:47
'''统计字符串中出现指定字符的次数'''


def get_count(s, ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count


if __name__ == '__main__':
    s = 'asdasdasfcsdgfs'
    ch = input('输入要统计的字符串：')
    count = get_count(s, ch)
    print(f'{s}出现的次数是{count}')
