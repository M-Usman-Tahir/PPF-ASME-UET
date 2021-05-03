# class Pet:
#     def __init__(self, name, speak):
#         print('Pet is created')
#         self.name = name
#         self.speak = speak
    
#     def setName(self, Name):
#         self.name = Name
        
#     def show(self):
#         print('My name is', self.name)
#         print('I speak', self.speak)
    
# class Cat(Pet):
#     def __init__(self, name):
#         super().__init__(name, 'Meow')
#         print('Cat is created')
    
   

# class Dog(Pet):
#     def __init__(self, name):
#         super().__init__(name, 'Bark')
#         super().show()
    
# class Author:
#     def __init__(self, *name):
#         self.Names = []
#         for i in range(len(name)):
#             self.Names.append(name[i])

# class Book:
#     def __init__(self, name, publisher, price, author, *names):
#         self.name = name
#         self.publisher = publisher
#         self.price = price
#         self.author = author(names)
    
# B1 = Book('CS1', 'CE', 190, Author, 'Ali', 'Saif')
# print(B1.author.Names)

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return 'Point at ({}, {})'.format(self.x, self.y)
    
#     def __eq__(self, b):
#         if self.x == b.x and self.y == b.y:
#             return True
#         return False
    
#     def __add__(self, b):
#         return Point(self.x+b.x, self.y+b.y)
    
    

# p1 = Point(1, 3)
# p2 = Point(1, 4)
# # print(p1==p2)
# # print(p1, p2)
# print(p1 + p2)
        
class Employee:
    NumOfEmployees = 0
    # Num
    def __init__(self, name, job):
        self.name = name
        self.job = job
        Employee.NumOfEmployees +=1
    
    # def __del__(self):
    #     Employee.NumOfEmployees -=1
    
    @classmethod
    def Remove_Employee(cls):
        cls.NumOfEmployees -=1
    
    @staticmethod
    def add(a, b):
        print(a+b)
    

E1 = Employee('Ali', 'Clerk')
E2 = Employee('Saad', 'HeadClerk')
# print(E1.NumOfEmployees)
# E1.Remove_Employee()
# print(E2.NumOfEmployees)
Employee.add(2, 4)