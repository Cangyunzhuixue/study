# 覃晓
# 时间： 2022/3/31 0031 22:33
lst = [5, 3, 7, 8, 1, 2, 57]

print('排序前', lst, id(lst))
lst.sort()
print('升序排序后', lst, id(lst))
lst.sort(reverse=True)
print('降序排序后', lst)
lst.sort(reverse=False)
print(lst)
print('内置函数排序，产生新的对象')
lst1 = [5, 3, 64, 7]
print(lst1)
new_lst = sorted(lst1, reverse=True)
print(new_lst)
