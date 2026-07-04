# # class Student(object):
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
#
# class Student(object):
#     def __init__(self,name,age,info):
#         self.name=name
#         self.age=age
#         self.info=info
#
#     def do_eat(self):
#         print(self.name+"do eat")
#
#     def do_study(self):
#         print(self.name+"do study")
#
# student = Student("tom",12,"this is good student")
# # student.do_eat()
# # student.do_study()
#
#
# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def eat(self,food):
#         print(self.name+" do eat "+food )
#
# dog = Animal("tom",1)
# dog.eat("bound")

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print("Student.__del__")
#
#     def show_info(self):
#         print(f"Student.show_info name:${self.name} age:${self.age}")
#
# class Animal:
#     def __init__(self):
#         print("Animal.__init__")
#     def __del__(self):
#         print("Animal.__del__")
#
#     def show_info(self):
#         print("Animal.show_info")
# student = Student("Tom",12)
# dog = Animal()
# student.show_info()
# dog.show_info()
#
# class Engin:
#     def __init__(self,name):
#         print("Engin__init__")
#         self.name=name
#     def __del__(self):
#         print("Engin__del__")
#
#     def do_start_work(self):
#         print(f"${self.name} start_work")
#
# class Car:
#     def __init__(self,engine):
#         print("Car__init__")
#         self.engine=engine
#     def __del__(self)
#         print("Car__del__")
#
#     def do_start_work(self):
#         print(" Car start_work")
#         self.engine.do_start_work()
#
# car=Car(Engin("v8"))
# car.do_start_work()

# def do_open_file(file_name):
#     with open(file_name) as f:
#         print(f.read(-1))
#
# do_open_file("./CLAUDE.md")

def do_open_file2(file_name):
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
path = "./.claude/settings.local.json"
do_open_file2(path)


