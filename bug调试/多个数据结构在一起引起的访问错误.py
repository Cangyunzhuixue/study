# 覃晓
# 时间： 2022/4/14 0014 10:37
lst = [
    {'rating': [9.7, 2062397], 'id': '1292052', type: ['犯罪', '剧情'], 'title': '肖申克的救赎', 'actors': ['蒂姆·罗宾斯', '摩根·佛里曼']},
    {'rating': [9.6, 1528760], 'id': '121546', type: ['剧情', '爱情', '同性'], 'title': '霸王别姬',
     'actors': ['张国荣', '张丰毅', '巩俐', '葛优']},
    {'rating': [9.5, 1559181], 'id': '1292720', type: ['爱情', '剧情'], 'title': '阿甘正传', 'actors': ['汤姆·汉克斯', '罗宾·怀特']}]

name = input('输入你要查询的演员：')
for item in lst:  # item是字典
    act_lst = item['actors']  # 得到每个演员列表
    for actor in act_lst:  #
        if name in actor:
            print(actor+'出演了'+item['title'])
        pass
