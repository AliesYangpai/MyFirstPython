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

def do_print_str(str):
    print("===do_print_str===star")
    if not str:
        print(" error str is invalidate")
    else:
        print(f"len:{len(str)}")
        for i in str:
            print(i)
    print("===do_print_str===end")
do_print_str("hello")

