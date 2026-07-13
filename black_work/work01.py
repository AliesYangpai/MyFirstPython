# 01数据存储于运算
# 02数据的预算逻辑
# 03数据存储容器
# 04函数
# 05面向对象

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