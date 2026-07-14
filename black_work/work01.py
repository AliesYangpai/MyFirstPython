# 01数据存储于运算
# 02数据的预算逻辑
# 03数据存储容器
# 04函数
# 05面向对象
import statistics
from ast import dump
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
# 列表 list[]
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
# def collection_list_work4():
#     my_list1 = [1,4,3,2,5]
#     my_list2 = [4,8,6,7,5]
#
#     # merge_list = my_list1 + my_list2
#     merge_list = [*my_list1, *my_list2]
#     my_new_list = []
#     for item in merge_list:
#         if item not in my_new_list:
#             my_new_list.append(item)
#
#     my_new_list.sort()
#     print(my_new_list)
# collection_list_work4()

# 元组 ()
# def tuple_work1():
#     t1 = (1,2,3)
#     for el in t1:
#         print(el)
#     print(t1)
# tuple_work1()

# def tuple_work2():
#     t1 = (1,2,3,4,5,6,7,8,9)
#     first,*center,last = t1
#
#     my_list = [1,2,3,4,5,6,7,8,9]
#     new_list = [e** 2 for e in my_list]
#     print(new_list)
#     print(first)
#     print(center)
#     print(last)
#
# tuple_work2()

# def set_work1():
#     s1 = set()
#     for i in range(9):
#         s1.add(i)
#     print(s1)
#
#
# set_work1()

# 集合set
# def set_work2():
#     football_set = {"w", "x", "y", "z", "a", "b"}
#     basketball_set = {"a", "b", "c", "d", "e", "f"}
#     frechet_set = {"h", "i", "b", "d", "e", "f"}
#     art_set = {"a", "b", "e", "f", "g", "t"}
#
#     fa_set = frechet_set.intersection(art_set)
#     print(fa_set)
# set_work2()

# 字典
# def dict_work1():
#     dict1 = {
#         "a": 1,
#         "b": 2,
#         "c": 3,
#     }
#     dict2 = {
#         "d": 4,
#         "e": 5,
#         "f": 6,
#     }
#
#
#     list1 = [dict1, dict2]
#     for dict in list1:
#         for i, e in enumerate(dict):
#             print(i, e)
# dict_work1()

# 函数
# def fun_wort1(a,b,c):
#     return a * b * 2 + b * c * 2 + a * c * 2, a * b * c
# s,tji = fun_wort1(3,4,5)
# print(s,tji)

# num = 100
# def fun_wort2(a,b,c):
#     global num
#     num= 1000
#     return a+b+c
#
# print(fun_wort2(1, 2, 3))
# print(num)

# def fun_work3(**kwargs):
#     if kwargs.get('age'):
#         print(kwargs['age'])
#     if kwargs.get('gender'):
#         print(kwargs['gender'])
#
# fun_work3(age=15, gender='male')

# 将函数作为参数传递
# def fun_add(a,b):
#     return a+b
#
# def fun_calculate(a,b,add):
#     return add(a,b)
#
# print(fun_calculate(1,2,fun_add))

# lamuda

# work1 = lambda x,y:x*y
# def fun_lambda(x,y,work):
#     return work(x,y)
# print(fun_lambda(1,2,work1))


# def fun_lambda2(x, y):
#     ret = x + y
#     return lambda a: ret ** 2 + a
# work1 = fun_lambda2(1, 2)
# print(work1(3))