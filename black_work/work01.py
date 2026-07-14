# 01数据存储于运算
# 02数据的预算逻辑
# 03数据存储容器
# 04函数
# 05面向对象
import statistics
from audioop import avg

from openai import OpenAI


#####
# 01数据存储于运算
# def exchange_work():
#     a = 13
#     b = 16
#     temp = a
#     a = b
#     b = temp
#     print(f'a: {a}, b: {b}')
#
#
# exchange_work()

# def exchange_work2_with_draw():
#     amount = 10000
#     cash = input("enter you cash:")
#     print(f"you withdraw {cash},the left is {amount-int(cash)}")
#
# exchange_work2_with_draw()

#####
# 02数据的预算逻辑

# def condition_work1(score):
#     if score >= 680:
#         print("985 211")
#     else:
#         print("normal")
# condition_work1(89)


# def condition_work3():
#     account = "1111"
#     pass_word = "2222"
#     enter_account = input("enter your account:")
#     if enter_account == account:
#         enter_pass_word = input("enter your password:")
#         if enter_pass_word == pass_word:
#             print("all access")
#         else:
#             print("wrong password")
#     else:
#         print("wrong account")
# condition_work3()

# def condition_work4():
#     account1 = "admin"
#     pass_word1 = "666888"
#
#     account2 = "root"
#     pass_word2 = "99999"
#
#     account3 = "zhangsan"
#     pass_word3 = "123456"
#
#     enter_account = input("enter your account:")
#     enter_pass_word = input("enter your password:")
#     if enter_account == account1 and enter_pass_word == pass_word1:
#         print(f"access {account1}")
#     elif enter_account == account2 and enter_pass_word == pass_word2:
#         print(f"access {account2}")
#     elif enter_account == account3 and enter_pass_word == pass_word3:
#         print(f"access {account3}")
#     else:
#         print("wrong account or password")
#
# condition_work4()

# def condition_work5():
#     num = input("Enter a number: ")
#     match int(num):
#         case 1:
#             print("1111")
#         case 2:
#             print("2222")
#         case 3:
#             print("3333")
#         case _:
#             print("others~~~")
#
# condition_work5()

# def loop_while_work():
#     i = 0
#     while i < 10:
#         print("wo yao xue xi")
#         i+=1
# loop_while_work()

# def loop_while_work2():
#     num = 1
#     sum = 0
#     while num <= 100:
#         if num %2 == 0:
#             sum+=num
#         num+=1
#     print(sum)
# loop_while_work2()

# def loop_for_work3():
#     tip = "hello-work"
#     for e in tip:
#         print(e)
#
# loop_for_work3()

# def loop_for_work4():
#     sum = 0
#     for e in range(1,100):
#         if e %2 !=0:
#             sum+=e
#
#     print(sum)
#
# def loop_for_work5():
#     sum = 0
#     for e in range(100,500):
#         if e %3 ==0:
#             sum+=e
#     print(sum)
# loop_for_work4()
# loop_for_work5()

# def loop_all_work6():
#     account1 = "admin"
#     pass_word1 = "666888"
#     account2 = "root"
#     pass_word2 = "99999"
#     account3 = "zhangsan"
#     pass_word3 = "123456"
#
#     while True:
#         enter_account = input("enter account: ")
#         enter_password = input("enter password: ")
#         if enter_account == account1 and enter_password == pass_word1:
#             print(f"{enter_account} is working")
#             break
#         elif enter_account == account2 and enter_password == pass_word2:
#             print(f"{enter_account} is working")
#             break
#         elif enter_account == account3 and enter_password == pass_word3:
#             print(f"{enter_account} is working")
#             break
#         else:
#             print(f"{enter_account} is not working,re_enter")
# loop_all_work6()

#####
# 03数据存储容器
# def collection_list_work1():
#     students = ["tom","jerry","torch"]
#     students.append("lorra")
#     if 'jerry' in students:
#         students.remove("jerry")
#     for student in students:
#         print(student)
#
# collection_list_work1()

# def collection_list_work2():
#     students = ["tom","jerry","torch","lorra","jim"]
#     new_student = students[0:3] #切片，实际上就是截取数据
#     print(id(students))
#     print(id(new_student))
#
#     for e in new_student:
#         print(e)
#
# collection_list_work2()

# def collection_list_work3():
#     my_list = []
#     count = 0
#     while count <10:
#         num = int(input("请输出数字："))
#         my_list.append(num)
#         count += 1
#     my_list.sort()
#     print(f"max:{my_list[0]} min:{my_list[9]} avg:{statistics.mean(my_list)} avg:{sum(my_list)/len(my_list)}")
#
# collection_list_work3()

# 去重处理
def collection_list_work4():
    my_list1 = [1,4,3,2,5]
    my_list2 = [4,8,6,7,5]

    # merge_list = my_list1 + my_list2
    merge_list = [*my_list1, *my_list2]
    my_new_list = []
    for item in merge_list:
        if item not in my_new_list:
            my_new_list.append(item)

    my_new_list.sort()
    print(my_new_list)
collection_list_work4()

