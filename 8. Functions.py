## Functions - is a block used to define the process (small program used frequently)


## Variable - use to define the data value, to be used frequently

### Type of functions
    # Built in function (Add, print, input, Max, min etc...)
    # user define function

## Steps to follow

    # define the function block
    # call the function

# def display():
#     print("Python")

# display()
# display()
# display()
# display()

# for i in range(10):
#     display()

# display()

def evenodd(n):  # n is called parameter of function (variable defined in function defination is parameter)
    """This is even odd function to identify weather the integer is even or odd """

    if n%2==0:
        print("Even")
    else:
        print("Odd")

# evenodd(5) # 5 is argument value 

# x=int(input("Enter a number: "))

# evenodd(x) # X is an argument value (value passed by function calling is argument value)

def multiply(n1,n2):
    n3 = n1*n2
    print("Result:",n3)
# multiply(2,4)

# in above program all the varible can be used in function only,


# def multiply(n1,n2): # parameters cannot be global (n1 and n2 cannot be global)
#     global n3   # This is used to make the variable global (Can be used outside the function)
#     n3 = n1*n2
#     print("Result:",n3)
# multiply(2,4)

# print(n3)

#----------------------------------------------------------------------------

## Default parameter- providing value for all the variable in parameter

# def add(n1=0,n2=0):
#     print("Addition",n1+n2)
# # add(4,3)

# add()
# add(3)
# add(5,6)

#------------------------------------------------------------------------------------------

## keyword argument - 
# In Python, a keyword argument is an argument passed to a function or method in the form keyword=value. When you call a function or method and provide keyword arguments, you explicitly specify which parameter each argument is intended to be matched with, regardless of their order.

# def add(n1=0,n2=0):
#     print("Addition",n1+n2)

# add(2,4)

# add(n2=5, n1=6)

#------------------------------------------------------------------------------------------

## Return value

# A return value in Python refers to the value that a function returns when it finishes executing. When a function completes its task, it can optionally send back a value to the code that called it using the return statement.


# def multiply(n1,n2):
    # return n1*n2

# print(multiply(3,4))
# x=multiply(3,4)
# print(x)

# s="python"
# print(s.upper())


#---------------------------------------------------------------------------------------

## Arbitrary Arguments
# In Python, you can define functions that accept an arbitrary number of arguments using the *args syntax. These arguments are treated as a tuple within the function, allowing you to pass any number of arguments when calling the function.

# in this it will give onlt value

# Collection example

# def getvalue(*a):
#     print(a)
# getvalue(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,90,1,2,3,4,5,6,7,7,8,9,0)


# Decollection example

# def add(a,b,c):
#     print("Result:",a+b+c)

# l=[2,4,1]

# add(*l)

#------------------------------------------------------------------------------


## Keyword Arbitrary arguments


# In Python, you can define functions that accept an arbitrary number of keyword arguments using the **kwargs syntax. These keyword arguments are treated as a dictionary within the function, allowing you to pass any number of keyword arguments when calling the function.

# in this it will give key as well as value

# def getvalue(**a):
#     print(a)

# getvalue(x=0,y=10,z=34)
# getvalue(a=12,b=54,c=1)
# getvalue(m=1,n=4)

#--------------------------------------------------------------------------------------------

# 1. Write a Python function to find the Max of three numbers. 

# def find_max(n1, n2, n3):
#     if n1>n2 and n1>n3:
#         return (n1,"is Max")
#     elif n1<n2 and n2>n3:
#         return (n2,"is Max")
#     else:
#         return (n3,"is Max")
# print(find_max(7,5,9))


# 2. Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def add(a,b,c,d,e):
#     return(a+b+c+d+e)
# l= [8, 2, 3, 0, 7]
# print(add(*l))


# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336

# def mult(a,b,c,d,e):
#     return(a*b*c*d*e)
# l= [8, 2, 3, -1, 7]
# print(mult(*l))



# 4. Write a Python program to reverse a string. 
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

# def rev_string(s):
#     revd_string=s[::-1]
#     return revd_string
# s="1234abcd"
# print(rev_string(s))

#-------------------------------------------------------------------------------------------------

# 5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. 

# def factorial(n):
    
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)   
        
# number = int(input("Enter a number: "))

# if number<0:
#     print("Enter a positive number")
# else:
#     print("Factorial of", number, "is:", factorial(number))


# 6. Write a Python function to check whether a number is in a given range. 

# def is_in_range(number, min_range, max_range):

#     return min_range <= number <= max_range

# min_range = int(input("Enter min value: "))
# max_range = int(input("Enter max value: "))
# number = int(input("Enter the number: "))

# if is_in_range(number, min_range, max_range):
#     print(number, "is in the range","[",min_range,max_range,"]")
# else:
#     print(number, "is not in the range","[",min_range,max_range,"]")



# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def char_count(string):
#     upper=0
#     lower=0
#     for i in string:
#         if i>='a' and i<='z':
#             lower+=1
#         elif i>='A' and i<='Z':
#             upper+=1
#     return("No. of Upper case characters :",upper,"\nNo. of lower case characters :",lower)
# string= "The quick Brow Fox" # input("Enter a String")
# print(*char_count(string))



# 8. Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique(l):
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    return("Unique list:",l1)
# l=[1,2,3,3,3,3,4,5]
# print(unique(l))

# 9. Write a Python function that takes a number as a parameter and check the number is prime or not. 
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# def number(num):
#     count=0
#     i=1
#     if num>0:
#         while i<=num:
#             if num%i==0:
#                 count=count+1
#             i+=1
#         if count==2:
#             return(num,"is Prime")
#         else:
#             return(num,"is not Prime")    
#     else:
#         return("Please enter a valid number")
# num=int(input("Enter a number: "))
# print(number(num))

# 10. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

# def even(l):
#     l1=[]
#     for i in l:
#         if i%2==0:
#             l1.append(i)
#     return l1
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even(l))


#---------------------------------------------------------------------------------------------

# Different properties of function

# display=print
# display(1,2,3,4,5,6,7)


## Function can be passed as an argument to a function

# def abc(f):
#     print("ABC function")
#     f()

# def xyz():
#     print("xyz function")
# def mnp():
#     print("mnp function")

# abc(xyz)
# abc(mnp)

## Nested function

# def outer():
#     def inner():
#         print("inner function")
#     print("Outer function")
#     inner()

# outer()


# def outer():
#     def inner(n):
#         print("Inner function",n)
#     print("Outer function")
#     return inner    
# x=outer()
# x(7)



## lambda function
    # unnamed function
    # one liner function (shorthand function)
    # lambda does't required return keyword to retun the value

# x=lambda : print("python")
# x()

# x= lambda s:s[::-1] 

# print(x("python"))


## Recursion -- When a function all itself, this is called recursion

# def disp():
#     print("python")
#     disp()
# disp()

# Function cannot be called infinit time, bcoz it will create new memory each time

def disp(n):
    if n>=1:
        print(n,"python")
        disp(n-1)
# disp(5)