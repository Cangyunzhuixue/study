# 覃晓
# 时间： 2022/4/17 0017 11:11
import os

filename = 'student.txt'


def menum():
    print('================学生信息管理系统====================')
    print('----------------功能菜单---------------------------')
    print('\t\t\t\t\t\t1、录入学生信息')
    print('\t\t\t\t\t\t2、查找学生信息')
    print('\t\t\t\t\t\t3、删除学生信息')
    print('\t\t\t\t\t\t4、修改学生信息')
    print('\t\t\t\t\t\t5、排序')
    print('\t\t\t\t\t\t6、统计学生总人数')
    print('\t\t\t\t\t\t7、显示所有学生信息')
    print('\t\t\t\t\t\t8、退出系统')
    print('-------------------------------------------------')


def main():
    while True:
        menum()
        choice = int(input('请选择:'))
        if choice in range(0, 8):
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('感谢使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()


def insert():  # 录入信息并且保存在磁盘文件中
    student_list = []
    while True:
        id = input('请输入Id（如1001）')
        if not id:  # 如果id是空的,退出循环
            break
        name = input('请输入姓名：')
        if not name:
            break

        try:
            english = int(input('请输入英语成绩'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入Java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的信息保存在字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('是否继续添加？y/n、')
        if answer == 'y':
            continue
        else:
            break
    # 调用save（）保存在文件中
    save(student_list)
    print('学生信息录入完毕')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')  # 如果没有这个文件可能会出差错
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            student_list = rFile.readlines()
    else:
        print('无学生信息')
        return
    student_id = input('输入要查找的学生ID：')
    for item in student_list:
        d = dict(eval(item))
        if d['id'] == student_id:
            print(d)


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_list = file.readlines()  # 读取了文件所有信息
            else:
                student_list = []
            flag = False
            if student_list:
                with open(filename, 'w', encoding='utf-8') as wFile:
                    d = {}
                    for item in student_list:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:  # 如果不是所要删除的，重新覆盖写一遍
                            print(d['id'] == student_id)
                            print('字典内id：', d['id'])
                            print('输入的id：', student_id)
                            wFile.write(str(d) + '\n')
                            print(str(d))
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后重新显示所有学生
            answer = input('是否继续删除？y/n')
            if answer == 'y':
                continue
            else:
                break
    pass


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('输入要修改的学员信息的id：')
    d = {}
    with open(filename, 'w', encoding='utf=8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print("招到学生信息，可以修改相关信息了")
                while True:
                    try:
                        d['name'] = input('输入姓名')
                        d['english'] = input('输入英语成绩')
                        d['python'] = input('输入python成绩')
                        d['java'] = input('输入java成绩')
                    except:
                        print('输入有误，重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否继续修改其他学生信息y/n\n')
        if answer == 'y':
            modify()


def sort():
    pass


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            student_list = rFile.readlines()
    else:
        print('无学生信息')
        return
    print(student_list.__len__())
    pass


def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            student_list = rFile.readlines()
    else:
        print('无学生信息')
        return
    for item in student_list:
        print(item)

    pass


if __name__ == '__main__':
    main()
