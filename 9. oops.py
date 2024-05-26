## OOPs (object oriented programming Structure) - if a function is defined in a class it is called OOPs. we define function inside the class

# OOPS is base on classes

## procedural oriented programming Structure - if everything work of the bases of function (or def as function). it is based on process (function)


# Class - it is a defination block to define multiple functions. function defined in call are called methods. we also have data attributes (variable in which data has been stored)


# object- it is a variable use to access the defination of a function. multiple objects can de defined in same class.

# Calling a class - when you call a class an object has been created.

# Attribute=charater sticks

# class store:
#     # Class Attribute 
#     store_name="Big Market"
#     location="Ghaziabad"
#     contact="879797878"
#     categories=["Electronics", "fashion","Grocery","Sports", "Toys"]

#     def __init__(self, name):
#         print("Welcome to our store", self.store_name)
#         self.name=name

#     # each method should have atlease 1 parameter for calling the object, its standered name is self
#     # def Entry(self, name):
#     #     self.name=name # here self.name is instant attribute
#     #     print("Welcome to our store", name)

#     def select_category(self,category): # category is instance Attribute (this data is an object)
#         print("Hello", self.name)
#         if  category in self.categories:
#             print("selected category is", category)
#         else:
#             print("Catagory not avalable")

#     def electronics(self):
#         print("Welcome to electronics department")

#     def fashion(self):
#         print("Welcome to fashion world")

#     def __del__(self):
#         print("object destroyed")    

# user1=store("Rahul")
# # print(user1.store_name)
# # user1.Entry("Rahul")    # Entry(user1)
# user1.select_category("Electronics")

# user2=store()
# user2.Entry("Rohit")
# user2.select_category("fashion")

# user3=store()
# print(user3.store_name)        


#------------------------------------------------------------------------

# Constructor -- Default method of a class. method name is (__init__). it is used to give memory to the object (user) and attributs. we call it with the name of class, in able example (user1=store()- this has called the cunstructor)
# Destructor -- Default method of a class. method name is (__del__). it is used to remove memory to the object (user) and attributs

# class ABC:
#     pass
# abc=ABC()


# Exercise 5. Computation class 
# 1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

# 1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
class Computation:

    # 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
    def factorial(self, n):
        m=1
        for i in range (n,0,-1):
            m=m*i
        return m
    
    # 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
    
    def sum(self, n):
        return sum(i for i in range(1,n+1))
    
    # 4 - Create a method called testPrime() in  the Calculation class to test the primality of a given integer. Test this method.
    
    def testPrime(self, num):
        """Check if a number is prime."""
        if num <= 1:
            return (num, "is not a prime number")
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return (num, "is not a prime number")
        return (num, "is a prime number")
        

    # 4 - Create  a method called testPrimes() allowing to test if two numbers are prime between them.
    
    #Error
    def testPrime(self, start,end):
        prime=[]
        for num in range(start, end+1):
            if num <= 1:
                return "No prime numbers between",start,"and",end
            for i in range(2, num//2 + 1):
                if num % i == 0:
                    break
            else:
                    prime.append(num)
        return "Prime numbers between",start,"and",end,"are",prime
    # Error
        
    # def testPrimes(self,start, end):
    #     primes = []
    #     for num in range(start, end+1):
    #         if num > 1:
    #             is_prime = True
    #             for i in range(2, int(num**0.5) + 1):
    #                 if num % i == 0:
    #                     is_prime = False
    #                 break
    #         if is_prime:
    #             primes.append(num)
    #     if primes:
    #         return "Prime numbers between {} and {} are {}".format(start, end, primes)
    #     else:
    #         return "No prime numbers between {} and {}".format(start, end)

    

   
    # 5 - Create a tableMult() method which creates and displays the multiplication table of a given 

    def tableMult(self,num):
        for i in range (1,11,1):
            print(num,'*',i,'=',num*i)


    # Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

    def allTablesMult(self):
        for i in range(1,10,1):
            for j in range (1,11,1):
                print(i,'*',j,'=',i*j)

    # 6 - Create a static listDiv() method that gets all the divisors of a given integer on new list called  Ldiv

    def listDiv(self, num):
        Ldiv=[]
        for i in range(1,num,1):
            if num%i==0:
                Ldiv.append(i)
        return Ldiv

    # Create another listDivPrim() method that gets all the prime divisors of a given integer.   

    def listDivPrim(self, num):
        Ldiv=[]
        for i in range(1,num,1):
            if num%i==0:
                for j in range(2, int(num**0.5) + 1):
                    if i % j != 0:
                     Ldiv.append(j)
                return Ldiv       
    
    
obj1= Computation()
# print(obj1.factorial(5))
# print(obj1.sum(5))
# print(obj1.testPrime(9))
print(obj1.testPrime(2,9))  #error
# obj1.tableMult(5)
# obj1.allTablesMult()
# print(obj1.listDiv(12))
# print(obj1.listDivPrim(12))

# # Exercise 3. Bank Account class: 
# # 1.	Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# # 2.	Create a constructor with parameters: accountNumber, name, balance.
# # 3.	Create a Deposit() method which manages the deposit actions.
# # 4.	Create a Withdrawal() method  which manages withdrawals actions.
# # 5.	Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# # 6.	Create a display() method to display account details.
# # 7.	Give the complete code for the  BankAccount class.

# class BankAccount:
    
#     def __init__(self, accountNumber,name,balance):
#         # Initialize the BankAccount object with account number, name, and balance.
#         self.accountNumber=accountNumber
#         self.name=name
#         self.balance=balance
    
#     def Deposit(self,amt):
#         # Add the given amount to the account balance.
#         self.balance=self.balance+amt  
    
#     def Withdrawal(self,amt):
#         # Subtract the given amount from the account balance.
#         self.balance=self.balance-amt 
    
#     def bankFees(self):
#         # Apply a 5% bank fee to the account balance.
#         self.balance=self.balance-(self.balance*0.05)
        
#     def display(self):
#         # Display account information including account number, name, and balance.
#         print ("your account number is", self.accountNumber)
#         print ("your name is", self.name)
#         print ("your account balance is", self.balance)


# obj1=BankAccount(12345,"Ajay", 5000)
# # # obj1.Deposit(500)
# # # print(obj1.Withdrawal(1000))
# # # obj1.bankFees()
# # print(obj1.display()) # Error none
# # # print(obj1.balance)
        

#---------------------------------------------------------------------------------------------

## Feature of OOPS
    # Inheritance
        # Single inheritance
        # Multiple inheritance
        # Multilevel inheritance
        # hierarichal inheritance
    # Polymorphism
    # Encapsulation
    # Abstraction

## Inherintance - one class features can be used by another class


## This is an example of single inheritance
# class vehicle:      # this is called parent class or base class
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")

# class car(vehicle):  # one class inheriated another class # this is called child class or derived class
#     pass

# mg=car()
# mg.start()

# ## This is an example of multiple inheritance  

# class vehicle:      # this is called parent class or base class
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")

# class Design:
#     def interior(self):
#         print ("interior Design")
#     def exterior(self):
#         print ("exterior Design")            

# class car(vehicle,Design):  # one class inheriated another class # this is called child class or derived class
#     pass

# mg=car()
# mg.start() 
# mg.interior() 


## This is an example of multilevel inheritance  

# class vehicle:      # this is called parent class or base class
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")

# class Design:
#     def interior(self):
#         print ("interior Design")
#     def exterior(self):
#         print ("exterior Design")            

# class car(vehicle,Design):  # one class inheriated another class # this is called child class or derived class
#     pass

# class sportscar(car):  # this is multilevel inhiretance, in this we have inhireted car, which has inheriated vehicle,Design class
#     pass

# ferrari=sportscar()
# ferrari.start()


# ## This is an example of hierarichal inheritance  


# class vehicle:      # this is called parent class or base class
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")

# class Design:
#     def interior(self):
#         print ("interior Design")
#     def exterior(self):
#         print ("exterior Design")            

# class car(vehicle,Design):  # one class inheriated another class # this is called child class or derived class
#     pass

# class sportscar(car):  # this is multilevel inhiretance, in this we have inhireted car, which has inheriated vehicle,Design class
#     pass

# # herirical inheritance
# class bus(vehicle):
#     pass
# class Truck (vehicle):
#     pass

# ferrari=sportscar()
# ferrari.start()


# class vehicle:      # this is called parent class or base class
#     def __init__(self, no_wheels):
#         self.no_wheels=no_wheels
        
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")

# class Design:
#     def interior(self):
#         print ("interior Design")
#     def exterior(self):
#         print ("exterior Design")            

# class car(vehicle,Design):  # one class inheriated another class # this is called child class or derived class
#     pass

# class sportscar(car):  # this is multilevel inhiretance, in this we have inhireted car, which has inheriated vehicle,Design class
#     pass

# # herirical inheritance
# class bus(vehicle):
#     pass
# class Truck (vehicle):
#     pass

# mg=car(4)
# mg.start() 
# mg.interior() 


# Exercise 1. Rectangle class:  
# 1.	Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# 2.	Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
# 3.	Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.
# 4.	Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.


# # Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
#     def Area (self):
#         self.a=self.length*self.width
#     def Perimeter(self):
#         self.p=2*(self.length+self.width)
#     def display(self):
#         print("Length:",self.length)
#         print("width:",self.width)
#         print("Area:",self.a)
#         print("Perimeter:",self.p)
    
# class Parallelepipede(Rectangle):
#     def volume(self,height):
#         self.height=height
#         print("volume:",self.length*self.width*self.height)

# pp=Parallelepipede(3,5)
# pp.Area()
# pp.Perimeter()
# pp.display()
# pp.volume(4)

# if  we make constructer in both the classes, below is the example for same.  

# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
#     def Area (self):
#         self.a=self.length*self.width
#     def Perimeter(self):
#         self.p=2*(self.length+self.width)
#     def display(self):
#         print("Length:",self.length)
#         print("width:",self.width)
#         print("Area:",self.a)
#         print("Perimeter:",self.p)
    
# class Parallelepipede(Rectangle):
#     def __init__(self, length, width, height):
#         self.height=height
#         Rectangle.__init__(self,length, width)
#     def volume(self):
#         print("volume:",self.length*self.width*self.height)

# pp=Parallelepipede(3,5,5)
# pp.Area()
# pp.Perimeter()
# pp.display()
# pp.volume()



# 1.	Create a Python class Person with attributes: name and age of type string.
# 2.	Create a display() method that displays the name and age of an object created via the Person class.
# 3.	Create a child class Student  which inherits from the Person class and which also has a section attribute.
# 4.	Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
# 5.	Create a student object via an instantiation on the Student class and then test the displayStudent method.

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print ("Student name is:",self.name)
#         print("Student age is:", self.age)
# class student(Person):
#     def __init__(self, section,name,age):
#         self.section=section
#         Person.__init__(self,name,age)
#     def displayStudent(self):
#         print("Student section is:",self.section)

# id=student(12,"Ajay",18)
# id.display()
# id.displayStudent()

# Exercise 8 Class String 
# Coding a class named myString inheriting from the str class allowing to endow strings with append() and pop () methods doing the same operations as those of lists class.


# class mystring(str):
#     def append(self,data):
#         return self+data
#     def pop(self,index):
#         return self.replace(self[index],"")

# obj=mystring("python")

# print(obj.upper())
# print(obj.append(" program"))
# print(obj.pop(3))


   ##-----------------------------------------------------------------------------
## Polymorphism-- many forms (multiple format)     
        # method overloading
        # method overriding
        # operator overloading

# method overloading - giving default value while defining variable in method. it can be done in constracter as well.

# example
# class calculator:
#     def add(self, num1=0, num2=0): 
#         return num1+num2

# a=calculator()

# print(a.add(6,5))
# print(a.add())
        
# method overriding - overriding parent class method by chiled class

#example
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print ("Student name is:",self.name)
#         print("Student age is:", self.age)
# class student(Person):
#     def __init__(self, section,name,age):
#         self.section=section
#         super().__init__(name,age)
#     def displayStudent(self):
#         print("Student section is:",self.section)

# id=student(12,"Ajay",18)
# id.display()
# id.displayStudent()


# operator overloading - we can customise the use of operator (exp we can use add to substract)

# a=2  # its class is int
# b=3  # its class is int   

# print(a+b)
# print(a.__add__(b))

# s='a'  # its class is string
# s1='b' # its class is string 

# print(s.__add__(s1))

# Example

# class calculator:
#     def __init__(self,a):
#         self.a=a
#     def __add__(self,other):
#         return self.a-other.a    

# x=calculator(6) 
# y=calculator(7)  

# print(x+y)  ## output is -1

# print(x.__add__(y))            #__add__(x,y)


#------------------------------------------------------------------------------

## Encapsulation-  it has been applyed on attributes, we can put different property data togeather (banding the data)

# public attribute- can be accessed by object.
# private attribute - cannot be accessed by object.

# class app:
#     def register(self, username, password):
#         self.username=username  # usename is a public attribute
#         self.__password=password  # password is a private attribute
        
#     def login(self, user, password):
#         if user==self.username and password==self.__password:
#             print("You are logged in")
#         else:
#             print("login failed")
#     def changepassword(self,newpass):        
#         self.__password=newpass


# obj=app()
# obj.register("abcd",1234)

# # print(obj.username)
# # print(obj.__password)
# # obj.login("abcd",1234)
# obj.changepassword(4321)
# obj.login("abcd",4321)

##---------------------------------------------------------------------

## Abstraction - it means hiding the methods, we can provide override method to end user

# from abc import ABC,abstractmethod

# class vehicle(ABC):      # this is called parent class or base class
#     def __init__(self, no_wheels):
#         self.no_wheels=no_wheels
#     @abstractmethod  
#     def start(self):
#         print("Vehicle Start method")
#     def run(self):
#         print("Vehicle Run method")
#     def stop(self):
#         print("Vehicle Stop method")         

# class car(vehicle):  
#     def start(self):
#         print("car Start method")
#         super().start()

# mg=car(4)

# mg.start()


#staticmethod

# class calculator():
#     @staticmethod
#     def iseven(n):
#         if n%2==0:
#             return True
#         else:
#             return False
# obj=calculator()

# print(obj.iseven(7))