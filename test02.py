# name = "tom"
# age = 22
# gender = True # True代表男，False 代表女
# newName = "jerry"
# newAge = 16
# newGender = False
#
# def showInfo (name, age, gender):
#     print("==========showInfo start")
#     if age > 18:
#         print(f"adaul name:{name}, age:{age},gender:{gender}")
#     else:
#         print(f"teenager name:{name}, age:{age},gender:{gender}")
#
# showInfo(name,age,gender)
# showInfo(newName,newAge,newGender)
from math import fabs

# 3.数据类型，int，float，bool，complex ,字符串,占位符
# num = 1
# def checkType(num):
#     print("===========checkType start")
#     print(f"{num} is {type(num)}")
#
# checkType(num)
# num2 = 1.00
# checkType(num2)
# checkType(True)
# checkType(True + False)
#
# name3 = "cristiano"
#
# def doPrintAgain(param):
#     print(f"value of param {param} type is {type(param)}")
#
# doPrintAgain(name3)
#
# def dozhanweifu(param1, param2):
#     print("my para1 : %s param2:%d" %(param1, param2) )
# name3 = "jj"
# age3 = 28
# dozhanweifu(name3, age3)

# 4 if判断，运算符，if-else ，if嵌套判断

# CARTYPE_YANGWANG = "yangwang"
# CARTYPE_DENZA = "denza"
# PLATFORM = "DI6"
#
#
# def checkCarInfo(carType, carPlatform):
#     if carType == CARTYPE_YANGWANG:
#         if carPlatform == PLATFORM:
#             print(f"finally this cartype is {carType} platform is {carPlatform}")
#         else:
#             print(f"unkonw plateform")
#     elif carType == CARTYPE_DENZA:
#         if carPlatform == PLATFORM:
#             print(f"finally this cartype is {carType} platform is {carPlatform}")
#         else:
#             print(f"unknow plateform")
#     else:
#         print(f" unkown car cartye:{carType} platform:{carPlatform}")
#
# checkCarInfo("wangchao","DI6")


# 5 循环语句，while，for ，break 和 continue

# def do_work_for_while(param):
#     while param < 10:
#         print(f"current value is {param} type is {type(param)}")
#         param += 1
#     print(f" final param:{param}")
#
# do_work_for_while(1)
#
# def do_work_for_for(param):
#     print("====do_work_for_for start")
#     for i in range(param):
#         print(f"all count:{param} this is :{i}")
#     print("====do_work_for_for end")
#
# do_work_for_for(5)
#
# def do_work_for_add_to_100(num):
#     print("====do_work_for_add_to_100 start")
#     i = 1
#     while i <= 100:
#         num+=i
#         i+=1
#     print(f"target is num:{num}")
#     print("====do_work_for_add_to_100 end")
#
# do_work_for_add_to_100(0)
#
# def do_work_for_for2(param):
#     print("====do_work_for_for2 start")
#     for i in range(param):
#         print(f"all count:{param} this is :{i}")
#     print("====do_work_for_for2 end")
#
# do_work_for_for2(6)

# 6 字符串编码，字符串常见操作，列表，列表常见操作

# def do_print_str(str):
#     print("===do_print_str===star")
#     if not str:
#         print(" error str is invalidate")
#     else:
#         print(f"len:{len(str)}")
#         for i in str:
#             print(i)
#     print("===do_print_str===end")
# do_print_str("hello")

# 7 列表 列表名=[a,b,c] 元素类型可以不一样
# list1 = [1, 44, 55, 1, 22]
#
#
# def do_show_list(list1):
#     for item in list1:
#         print(f"currentValue:{item}")
#     print(f"list1: {list1} type: {type(list1)}")
#
#
# do_show_list(list1)
#
# list2 = [1, 2, 3, 4]

#
# def do_add_value(param, list):
#     list.append(param)
#     print(f"do_add_value param:{param}")
#     return list
#
#
# def do_del_value(param, list):
#     flag = False
#     if param in list:
#         list.remove(param)
#         flag = True
#         print(f"list contains {param} do remove flag:{flag}")
#     print(f"list not contains {param} do remove flag:{flag}")
#     return flag
#
#
# def do_update_value(param, i, list):
#     flag = False
#     if 0 <= i < len(list):
#         list[i] = param
#         flag = True
#         print("update success")
#     else:
#         print("update error")
#     return flag
#
# def do_fetch_list(list):
#     print(f"list: {list}")
#
# def operate_work():
#     list = [1,2,3,4,5]
#     do_add_value(27, list)
#     do_fetch_list(list)
#
#     do_del_value(5, list)
#     do_fetch_list(list)
#
#     do_update_value(44,2,list)
#     do_fetch_list(list)
#
#
# operate_work()

# 8 元组，字典，集合
# def do_test_work():
#     trp = (1,6,"name")
#     list = [12,3,trp,5]
#     e =list.index(trp)
#     print(e)
#     print(list)
# do_test_work()
#
# def do_show_dic():
#     dic = {"name":"tom","age":17,"gender":"male"}
#     for key,value in dic.items():
#         print(key,value)
# do_show_dic()

# 9 类型转换，深浅拷贝，可变对象，不可变对象
# import copy
# def do_work_copy():
#     s1 = {1,66,69}
#     di = {"name":"tome","age":24}
#     list = [1,2,3,s1,di]
#     new_list =copy.copy(list)
#     print(f"list point:{id(list)} new_list point:{id(new_list)}")
#     print(f"s1 point:{id(list[3])} new_list.s1 point:{id(new_list[3])}")
#
# do_work_copy()

# 10 函数、返回、参数、函数嵌套
def do_work_9(*args , param =6):
    print(f"args:{args} param:{param}")

do_work_9(1,2,3,9,0)