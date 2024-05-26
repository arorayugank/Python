## String --Data type use to store test data.
    ##      -- Character data collection (character array)


# s='python's' - # this is invalid
# s1="python's " # this is correct
# s2= '"python"'- # output "python"

## Docstring - it can be used to mention multiline string

# s3= '''"python's"'''

# s4="""this is python
# this is one of the progrming language"""

# print(s3)
# print(s4)


## len function - used to know the length of string

# s4="""this is python
# this is one of the progrming language"""

# print(len(s4))

#---------------------------------------------------------------------------------------------

## indexing - is use to access single charcater in a string. this is represented by []

# s="python"

# print(s[0]) # output p
# print(s[5]) # output n
# print(s[-1]) # output n

#----------------------------------------------------------------------------------------

## Slicing - is use to access multiple charcater in a string. this is represented by []

# s="python program"

# print(s[2:5:1]) # tho

# print(s[7:14:1]) # program

# print(s[-7::1]) # program

# print(s[:6]) # python

# print(s[5::-1]) # nohtyp

# print(s[::-1]) # margorp nohtyp

# print(s[1:-1]) # ython progra

# print(s[-1:]) #m

## String formating - This is need to change some data in a string

# %s - for Syntax
# %d - for intiger
# %f - for float

# s=" %s Program"

# print (s%('python'))

# print (s%('Java'))



# s="I have enrolled in %s batch and my time is %d O'clock"

# course= input("Enter course:")
# t=int(input("Enter time:"))

# print(s% (course,t))



# s="I have enrolled in {} batch and my time is {} O'clock"

# course= input("Enter course:")
# t=int(input("Enter time:"))

# print(s.format(course,t)) # format function is used to mention the format of s, we can repet the data multiple time in this with index value below is the example. 

# s="I have enrolled in {0} batch and my time is {1} O'clock. {0} Trainer is well qualified"

# course= input("Enter course:")

# t=int(input("Enter time:"))

# print(s.format(course,t))


# course= input("Enter course:")

# t=int(input("Enter time:")) 

# s=f"I have enrolled in {course} batch and my time is {t} O'clock. {course} Trainer is well qualified"
# # f is used to format a string

# print(s)

#========================================================================================

## Operaters

# concatination - to joint two string is is represented bt +

# s1="Python"
# s2="program"

# print(s1+" "+s2)


#-----------------------------------------------------------------------------

# Multiplication - use to print string multiple time

# s1="Python"
# print((s1+" ")*5)

# s1="Python"
# s2="program"

# s1+=(" "+s2)
# print (s1)

# s2*=4
# print(s2)


#-----------------------------------------------------------------------------

## less then grater then

# s1="python"
# s2="program"
# print(s1>s2)

#-----------------------------------------------------------------------------

# ## equal operater

# print (s1==s2)

#-----------------------------------------------------------------------------

# ## in operater

# print('s' in s1)

## for loop

# s1="python"

# for i in s1:
#     print(i)

# ## while loop

# s1="python"
# i=0
# while i<len(s1):
#     print(s1[i])
#     i+=1

#========================================================================================

## method - pre defined function of string is called method

# s="python program"
# s1="PYTHON PROGRAM"

# print(s.capitalize()) ## output Python program

# print(s.upper()) ## output PYTHON PROGRAM

# print(s.title()) ## output Python Program

# print(s1.lower()) ## output python program

# print(s1.casefold()) ## output python program

# print(s.swapcase() ## output PYTHoN PROGRAM

# print(s.replace('python', 'Java'))  ## output Java program

# print(s.center(20,'-')) ## output ---python program---

# print(s.count('p')) ## output 2

# print(s.count('p',0,5)) ## output 1

# print(s.encode()) ## Change in byte data ## output b'python program'

# print(s.endswith('m')) ## check end char of string  ## output True

# print(s.startswith('p')) ## check start char of string  ## output True

# s="python\tprogram" #\t is use to give tab space between two words

# print(s.expandtabs(16))  # use to give expnad tab space between two words 

# print(s)

# print(s.index('y')) # to know index no. of a char in a string  ## output 1

# print(s.index('k')) ## this will give you an error

# print(s.index('p')) ## output 1

# print(s.index('p',1)) ## output 7

# print(s.index('o')) ## output 4

# print(s.index('o',5)) ## output 9

# print(s.find('o')) ## output 4

# print(s.find('o',5)) ## output 9

# print(s.find('o',10)) ## output -1 (means data not found), this will not give error

# print(s.split()) # this is use to split the string with words, check space and split ## output ['python', 'program']

# s="python,program"

# print(s.split(',')) # this is use to split the string with words, check char input and split acordingly

# l=['python', 'program']

# print(" ".join(l)) # to join two words in a list


# s="""python program
# Java program
# PHP program
# DS program"""

# print(s.splitlines()) # use to split according to line, it is done throught \n (new line) ## output is ['python program', 'Java program', 'PHP program', 'DS program']


# s=" python program "
# # print(s)
# # print(s.strip()) # remove space form start and end of line

# print(s.lstrip()) # remove space on left

# print(s.rstrip()) # remove space on right

# s="python program"
# print(s.rjust(20)) # justify on right (give space on left)

# print(s.ljust(20)) # justify on left (will not give the space as it is already been writen form left)


# s="pythonprogram"

# print(s.isalpha()) # Space is not an alphabate
# print(s.islower()) # output true
# print(s.isupper()) # output false
# print(s.isalnum()) # use to check is data is alpha numeric
# print(s.isdigit())
# print(s.isnumeric())
# print(s.isdecimal())

# s="           "
# print(s.isspace()) # to check if there is only space in string

# s="python"
# print(s.isascii()) # check if every char in string has ascii code

# s="python\n"
# print(s.isprintable()) # check if every char in string cna be printed. in this \n is non printable hence output will be False

#======================================================================

# 1.	Write a Python program to calculate the length of a string.
# s="python program"

# print(s.__len__())


#======================================================================

# 2.	Write a Python program to check whether an alphabet is a vowel or consonant

# s=input("Enter a alphabet")

# vowel='aeiouAEIOU'

# if s.isalpha() and len(s)==1:
#     if s in vowel:
#         print(s," is a vowel")
#     else:
#         print(s, " is a consonant")
# else:
#     print("Invalid char")

#======================================================================

# 4.	Write a Python program to check number of vowels consonants and digits and white spaces from a user input string.

# s=input("Enter a String: ")

# vowel='aeiouAEIOU'
# v=0
# c=0
# d=0
# ws=0
# for i in s:
#     if i.isalpha():
#         if i in vowel:
#             v+=1
#         else:
#             c+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         ws+=1
# print ("Vowel", v)          
# print ("con", c)
# print ("Digit", d)
# print("wide space", ws)


# ##### 5.	Program to Find the Frequency of Characters in a String.

# s=input("Enter a String: ")

# for i in s:
#     print("frequence of",i,':', s.count(i))



# 6.	Write a Python program to remove spaces from a given string.

# s=input("Enter a String: ")

# print(s.replace(" ", ""))



# 7.	Write a Python program to capitalize first and last letters of each word of a given string.

# s='python program'
# s1=""
# for i in s.split():
#     s1+=i[0].upper()+i[1:-1]+i[-1].upper()+" "
#     print(s1)

# print(s[0].upper()+s[1:-1]+s[-1].upper())


# ##### 9.	WAP to check a given string is palindrome(symetrical)

# s="nitin"

# if s==s[::-1]: # to revers a string
#     print("palindrome")
# else:
#     print("not palindrome") 

# 12.	find uncommon words from two string 

# s1="python program"
# s2="java program"
# result=""

# l1=s1.split()
# for i in l1:
#     if i not in s2:
#         result+=i

# l2=s2.split()
# for i in l2:
#     if i not in s1:
#         result+=i

# print(result)



# 11.	 find out the least and most frequent letter in a string


# s1="python program"

# a={}

# for c in s1:
#     if c in a:
#         a[c]+=1
#     else:
#         a[c]=1
# least=min(a,key=a.get)
# most=max(a,key=a.get)

# print(least)
# print(most)
