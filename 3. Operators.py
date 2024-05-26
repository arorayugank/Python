# Operators

# Arithmetic operator

# Arithmetic Operations:

# Addition: +
# Subtraction: -
# Multiplication: *
# Division: /
# Floor Division: // (returns the integer part of the division)
# Modulus (Remainder): %
# Exponentiation: ** (power = i power j)

# i=5
# j=7

# print(i+j)
# print(i-j)
# print(i*j)
# print(i/j)
# print(j%i)  # Reminder
# print(i**j)

#------------------------------------------------------



# Assignment operator

# Assignment Operations:

# An assignment operator is a symbol used in programming languages to assign a value to a variable. It is a fundamental concept in programming, allowing developers to store and manipulate data efficiently. In Python, the most common assignment operator is the equal sign (=).

# Here's a basic definition:

# Assignment Operator (=):

# The equal sign (=) is used to assign the value on the right side of the operator to the variable on the left side.
# It establishes a binding or association between the variable name (on the left) and the value (on the right).
# Syntax: variable = value
# Example: x = 10
# In addition to the basic assignment operator (=), there are compound assignment operators, which combine an arithmetic operation with assignment. These operators are shorthand for performing an operation and assigning the result back to the variable. Examples of compound assignment operators in Python include +=, -=, *=, /=, //=, %=, and **=.

# Here's a brief overview of compound assignment operators:

# +=: Add and assign
# -=: Subtract and assign
# *=: Multiply and assign
# /=: Divide and assign
# //=: Floor divide and assign
# %=: Modulus (remainder) and assign
# **=: Exponentiate and assign
# Compound assignment operators are commonly used to make code more concise and readable, especially when performing repetitive operations on variables.

# Assignment: =
# Augmented Assignment: +=, -=, *=, /=, //=, %=, **= 

# +=: This operator adds the value on the right to the variable on the left and assigns the result to the variable on the left.

# -=: This operator subtracts the value on the right from the variable on the left and assigns the result to the variable on the left.

# *=: This operator multiplies the variable on the left by the value on the right and assigns the result to the variable on the left.

# /=: This operator divides the variable on the left by the value on the right and assigns the result to the variable on the left

# //=: This operator performs floor division, dividing the variable on the left by the value on the right and assigning the integer result to the variable on the left

# %=: This operator calculates the modulus (remainder) when the variable on the left is divided by the value on the right and assigns the result to the variable on the left.

# **=: This operator raises the variable on the left to the power of the value on the right and assigns the result to the variable on the left

# i=4
# j=i
# # print(j)

# # # i+=j #this means i=i+j
# # i-=j # this means i=i-j
# # print(i)

# j*=i # this means 

# print(j)


#------------------------------------------------------------

# Comparison Operations 

# Comparison Operations: compaire b/w 2 things

# Equal to: ==
# Not equal to: !=
# Greater than: >
# Less than: <
# Greater than or equal to: >=
# Less than or equal to: <=

# plantA_height=20

# plantB_height=30

# print(plantA_height>plantB_height) #false

# print(plantA_height<plantB_height) #true

# print(plantA_height<=plantB_height) #true

# print(plantA_height>=plantB_height) #false

# print(plantA_height==plantB_height) #false

# print(plantA_height!=plantB_height) #true



#-----------------------------------------------------------


# Logical Operations:(and,or, not)

# AND: and- used in user name and password in login
# OR: or - Asking for ether email id or phone no. in login
# NOT: not - usend in multiple comprison

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# x= 18

# x=int(input("Enter a number:"))

# print(x>=1 and x<=50)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)


# print(not True)


#------------------------------------------------------------

#identity operater (is, is not)

# is: Checks if two variables refer to the same object.
# is not: Checks if two variables refer to different objects.


# identity operater check the memory address, so it can be used in Primitive Type of data only. it cannot be used in non primitive type of data because its memory address change every time.

# however Equal to: == operater work on value insice the variable, so it cam work on both types of data

# id: this function is used to check memory address

# i=3
# j=3

# print(i is j) # True
# print(i==j) # True

# i=[3,4]
# j=[3,4]

# print(i is j) # False
# print(i==j) # True

# print(id(i), id(j))

#-----------------------------------------------------------

#Membership Operations:

# in: Checks if an element is present in a sequence (list, tuple, string, etc.).

# not in: Checks if an element is not present in a sequence.



# l=['a',3,'python',75,8.5]

# print('a'in l) # True
# print(23 in l) # False

# s= "Rahul is in class"

# print('Rahul' in s) # True

# x=(float(input("Enter a number:")))

# print(x in range (1,51))
#------------------------------------------------------------





#===========================================================

# Conver metter to feet program

# meter=(float(input("Enter the lenth in meter:")))
# print("Distance in feet:", meter*3.28, "feet")

# Conver CM to feet program

# cm=(float(input("Enter the hight in cm:")))
# print("Distance in feet:", (cm*3.28)/100, "feet")



#===========================================================

# 4. write a program to find an input number is even .result is in True and False

# n=(int(input("Enter a number")))
# print(n%2==0)

# 2. write a program to covert a input tempreture in celcius to farenheit .

# tempc=(float(input("Enter Temprature in celcuis:")))

# f=(tempc*(9/5)) +32

# print("Tem in farenheit:",f)




