# Loops : Is a Block statement used to itrate change) the data. loop can be made in integer value only.

#Types of loops:
    # 1. While loop
    # 2. for loop
#----------------------------------------------------------------------------

# While loop - it work only on intiger

# i=1
# while i<=10:
    
#     print("Python",i)

#     i+=1
# print("i=", i)

# i=10
# while i>=1:
#     print(i)
#     i-=1
# print("i=", i)

#____-------------------------------------------------------------

## Write a program to display the multiplication table of a no.

# 5*1 = 5
# 5*2 = 10

# n=int(input("Enter a number"))

# i=1
# while i<=10:
#     print(n,'*',i,'=',n*i)
#     i+=1

## ----------------------------------------------------------

## Write a program to find the factors/divisors of a number

## eg n=6, divisors are 1,2,3,6

# n=int(input("Enter a no."))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1

#-------------------------------------------------------------

# to print each value in one line print(i,end=' ')
    
# n=int(input("Enter a no."))
# i=1
# while i<=n:
#     if n%i==0:
#         print(i,end=' ')
#     i+=1

#------------------------------------------------------------------

# Prime no. - those which can be divided with 1 and them self only

# 1. Write a program to check a number is prime or not

# n=int(input("Enter a no."))
# count=0
# i=1

# while i<=n:
#     if n%i==0:
#         count+=1
#     i+=1
# if count==2:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")

##-------------------------------------------------------------------------------------------

# 1,2,3,4,5......n

# 2. Accept n number from user and calculate the sum of all number between 1 and n including n

# n=(int(input("Enater a no: ")))
# s=0
# i=1
# while i<=n:
#     s=s+i
#     i+=1
# print("Sum:",s)    

# 1*2*3*4........*n

# n=(int(input("Enater a no: ")))
# s=1
# i=1
# while i<=n:
#     s=s*i
#     i+=1
# print("Multiplication:",s)    


# while True:
#     print("python")

#-----------------------------------------------------------------------------------------
# Break statment- if you want to break the loop in between

# i=1
# while i<=20:
#     print(i)
#     if i==10:
#         break
#     i+=1

# i=1
# while i<=20:
#     i+=1
#     if i%3==0:
#         continue
#     print(i)
    
#-----------------------------------------------------------------------------------------

## Else block

# i=1
# while i<=10:
#     print(i)
#     i+=1
# else:
#     print("Done")

# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i+=1
# else:
#     print("Done")

#--------------------------------------------------------------------------------------------

# Guess a number

# n=7
# i=1

# while i<=5:
#     k=int(input("Guess the no. b/w 1-9: "))

#     if k==n:
#         print("Well guessed")
#         break
#     else:
#         print("Wrong guess")  

#     i+=1
# else:
#     print("You loose the game")

#-----------------------------------------------------------------------------------------

# 3. Display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# i=1

# while i<=150:  
#     if i%5==0:
#         print(i)
#     i+=1
        
  

#---------------------------------------------------------------------------------------------

# 4. Given a number count the total number of digits in a number.

# number = input("Enter a number: ")
# total_digits = len(number)
# print("Total number of digits in",number,"is", total_digits)

# n = int(input("Enter a number: "))
# count=0
# while n>0:
#     n=n//10
#     count+=1
# print(count)
#---------------------------------------------------------------------------------------

# 5. Calculate the Sum of Natural Numbers

# n=int(input("Enter a no."))

# i=1
# s=0

# while i<=n:
#     s+=i
#     i+=1
# print(s)

#-----------------------------------------------------------------------------------

# 6. Find Factorial of a Number
      
#    5!=5*4*3**2*1=120

# n=int(input("Enter a no."))

# i=1
# s=1

# while i<=n:
#     s*=i
#     i+=1
# print(s)


# 8. Write a Python program to get the Fibonacci series between 0 to 50. 
#    Note : The Fibonacci Sequence is the series of numbers :
#    0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#   Every next number is found by adding up the two numbers before it.
#   Expected Output : 0 1 1 2 3 5 8 13 21 34


# fs=[]
# a=0
# b=1
# while b<50:
#     fs.append(b)
#     a=b
#     b=a+b
# print(fs)


# def generate_fibonacci_series(limit):
#     fibonacci_series = []
#     a, b = 0, 1
#     while a <= limit:
#         fibonacci_series.append(a)
#         a, b = b, a + b
#     return fibonacci_series

# # Set the upper limit
# # limit = int(input("Enter the number: "))
# limit=50

# # Generate and print Fibonacci series up to the limit
# fibonacci_series = generate_fibonacci_series(limit)
# print("Fibonacci series up to", limit, ":", fibonacci_series)

# # Prompting the user for the number of terms in the sequence
# n = int(input("Enter the number of terms: "))

# # Initializing the first two terms
# a, b = 0, 1

# # Printing the first two terms
# print("Fibonacci Sequence:")
# print(a)
# print(b)

# # Generating and printing the remaining terms
# for _ in range(2, n):
#     c = a + b
#     print(c)
#     a, b = b, c

#-------------------------------------------------------------------------------------------

# 9.  Find GCD(HCF) of two Numbers







# 20. Write a Python program to check the validity of password input by users. 
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.



#-----------------------------------------------------------------
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
# * * * * *

# row=1
# while row<=5:
#     col=1
#     while col<=5:
#         print('*', end=" ")
#         col+=1
#     print()
#     row+=1

#-----------------------------------------------------------------------------------

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# row=1
# while row<=5:
#     col=1
#     while col<=row:
#         print('*', end=" ")
#         col+=1
#     print()
#     row+=1

#---------------------------------------------------------------------------------------------

# * * * * * 
# * * * * 
# * * *  
# * * 
# * 

# row=5
# while row>=1:
#     col=1
#     while col<=row:
#         print('*', end=" ")
#         col+=1
#     print()
#     row-=1

#-------------------------------------------------------------------------

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


# row=1
# while row<=5:
#     col=1
#     while col<=row:
#         print('*', end=" ")
#         col+=1
#     print()
#     row+=1
# row=1
# while row<=4:
#     col=1
#     while col<=5-row:
#         print('*', end=" ")
#         col+=1
#     print()
#     row+=1    


#----------------------------------------------------------------------------------------------

# For loop - works on string,bytes,list,tuple,dict,set,frozenset,bytearray,range.

# Data in which for loop is applied is called itrables (can be itrated(collection))

# s= 'python'

# for i in s:
#     print(i)

# for i in range(1,11,1):
#     print(i)



# 1. check the prime no given from the user

# num=int(input("Enter a number: "))
# c=0
# i=1
# while i<=num:
#     if num%i==0:
#         c=c+1
#     i+=1    
# if c==2:
#     print("prime")    
# else:
#     print("not prime")    

# 13. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included). 

# r=range(1500,2701,1)

# for i in r:
#     if i%7==0 and i%5==0:
#         print(i)


# 16. Write a Python program that accepts a word from the user and reverse it. 

# s= input("Enter a word: ")
# s1=s[::-1]
# print(s1)


# 11. Display Characters from A to Z Using Loop

# alpha=[]

# for i in range(ord('A'),ord('Z')+1):
#     alpha.append(chr(i))
# print(alpha)


# 12. Reverse a Number

# num=int(input("Enter a Number: "))
# rev_num=0
# while num !=0:
#     rev_num=rev_num*10+num%10
#     num=num//10
# print(rev_num)

# def rev_num(num):
#     rev_num=0
#     # Reversing the number
#     while num !=0:
#         # Extracting the last digit of num and appending it to rev_num
#         rev_num=rev_num*10+num%10
#         # Removing the last digit from num
#         num=num//10
#     return rev_num

# num=int(input("Enter a Number: "))
# print(rev_num(num))



# 14. Write a Python program to guess a number between 1 to 9. 
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

# import random

# n=random.randint(1,9)

# i=1
# while i<=5:
#     g=int(input("Guess a number b/w 1-9:"))

#     if n==g:
#         print("Well guessed")
#         break
#     else:
#         print("You have",5-i," attempt left")
#     i+=1
# else:
#     print("You loose the game")


# 16. Write a Python program that accepts a word from the user and reverse it. 

# Word=input("Enter a word: ")
# rev_word=Word[::-1]
# print(rev_word)


# 17. Write a Python program to count the number of even and odd numbers from a series of numbers. 
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

# l=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("Number of even numbers :", even)
# print("Number of odd numbers :", odd)



# Amount=10000
# total=0
# i=1
# while i<=10:
#     intrest=(Amount*15)/100
#     i+=1
# Amount=Amount+intrest
# print(Amount)
# print(intrest)


# def calculate_compound_interest(principal, rate, time):
#     # Convert rate percentage to decimal
#     rate = rate / 100
    
#     # Calculate compound interest
#     amount = principal * (1 + rate) ** time
#     return amount
    
   

# # Given values
# principal = 10000  # Principal amount
# rate = 15  # Interest rate (in percentage)
# time = 10  # Time period (in years)

# # Calculate compound interest
# interest = calculate_compound_interest(principal, rate, time)

# # Print the result
# print("Compound Interest:", round(interest, 2))
