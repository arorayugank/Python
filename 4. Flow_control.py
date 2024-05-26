## flow control

    # if block
    # else block
    # if elif block
    # Nested if or nested else block

# we use ':' to make a block

# Space in block is called indentation

# Check and print if number entered is even or odd

# n=int(input("Enter a number: "))

# if n%2==0:
#     print(n,"is even number")
#     print(n,"is a positive number")
# else:
#     print(n,"is an odd number")

# Age= int(input("Enter Your Age:"))
# if Age>=18:
#     print("You are eligable to cast the vote")
# else:
#     print("You are not eligable to cast the vote")

# year= int(input("Enter Year:"))
# if year%4==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is a not leap year")

# phy= int(input("Enter Your phy marks:"))
# chem= int(input("Enter Your chem marks:"))
# maths= int(input("Enter Your maths marks:"))
# if phy>=60 and chem >=55 and maths>=65:
#     print("Eligible to take admission")
# else:
#     print("Not eligible to take admission")

#-----------------------------------------------------
## nested if- there are multime if condition then it is nested if


# 1. Write a Python Program to read the age of a candidate and determine whether it is eligible for casting his/her own vote. 
# Test Data : 21
# Expected Output :
# Congratulation! You are eligible for casting your vote.

# Age= int(input("Enter Your Age:"))
# if Age>=18:
#     print("Congratulation! You are eligible for casting your vote.")
# else:
#     print("Sorry! You are not eligable to cast the vote.")


#----------------------------------------------------------

# 2. Write a Python Program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0. 
# Test Data : -5
# Expected Output :
# The value of n = -1
# m>0   n=1
# m==0  n=0
# m<0   n=-1

# m=(int(input('Enter a number: ')))

# if m>0:
#     print('The value of n = 1')
# elif m==0:
#     print('The value of n = 0')
# else:
#     print('The valu of n = -1')    


# m=int(input("Enter a number: "))

# if m>0:
#     print("The value of n = 1")
# elif m<0:
#     print("The value of n = -1")
# else:
#     print("The value of n = 0")

#------------------------------------------------------------

# 3. Write a Python Program to accept the height of a person in centimeter and categorize the person according to their height. 
# Test Data : 135
# Expected Output :
# The person is Dwarf.
# Categories:
# <140  Dwarf
# >=140  <=170  Average 
# >=170  Tall


# height=(int(input("Enter person's height in CM: ")))

# if height>0 and height<140:
#     print('The person is Dwarf')
# elif height>=140 and height<=170:
#     print('The person is Average')
# elif height>=170:
#     print('The person is Tall')
# else:
#     print('Please enter the height in positive number')






# height=int(input("Enter the height in CM: "))

# if height>0 and height<140:
#     print("The person is Dwarf")
# elif height>=140 and height<=170:
#     print("The person is Average")
# elif height>170:
#     print("The person is Tall")
# else:
#     print("Please enter the height in positive number")

#------------------------------------------------------------

# 4. Write a Python Program to find the largest of three numbers. 
# Test Data : 12 25 52
# Expected Output :
# 1st Number = 12,        2nd Number = 25,      3rd Number = 52
# The 3rd Number is the greatest among three

# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# num3=int(input("Enter 3rd number: "))

# if num1>num2 and num1>num3:
#     print("The 1st Number is the greatest among three")
# elif num2>num1 and num2>num3:
#     print("The 2nd Number is the greatest among three")
# else:
#     print("The 3rd Number is the greatest among three")


#------------------------------------------------------------

# 5. Write a Python Program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
# Test Data : 7 9
# Expected Output :
# The coordinate point (7,9) lies in the First quadrant.


# x=int(input("X coordiante: "))
# y=int(input("Y coordiante: "))
# if x>0 and y>0:
#     print("The coordinate point (",x,",",y,") lies in the First quadrant")
# elif x<0 and y>0:
#     print("The coordinate point (",x,",",y,") lies in the second quadrant")
# elif x<0 and y<0:
#     print("The coordinate point (",x,",",y,") lies in the third quadrant")
# elif x>0 and y<0:
#     print("The coordinate point (",x,",",y,") lies in the forth quadrant")
# elif x==0 and y==0:
#     print("The coordinate point (",x,",",y,") lies in the center of axis")
# elif x!=0 and y==0:
#     print("The coordinate point (",x,",",y,") lies on X axis line")
# elif x==0 and y!=0:
#     print("The coordinate point (",x,",",y,") lies on Y axis line")

#---------------------------------------------------------------------------

# 6. Write a Python Program to find the eligibility of admission for a professional course based on the following criteria: 
# Eligibility Criteria : Marks in Maths >=65 and Marks in Phy >=55 and Marks in Chem>=50 and Total in all three subject >=190 or Total in Maths and Physics >=140 ------------------------------------- Input the marks obtained in Physics :65 Input the marks obtained in Chemistry :51 Input the marks obtained in Mathematics :72 Total marks of Maths, Physics and Chemistry : 188 Total marks of Maths and Physics : 137 The candidate is not eligible.
# Expected Output :
# The candidate is not eligible for admission.

# phy=int(input("Input the marks obtained in Physics: "))
# chem=int(input("Input the marks obtained in Chemistry: "))
# maths=int(input("Input the marks obtained in Mathematics: "))

# if maths >=65 and phy >=55 and chem>=50:
#     if (maths+phy+chem)>=190 or (maths+phy)>=140:
#         print("The candidate is eligible for admission")
# else:
#     print("The candidate is not eligible for admission")

#----------------------------------------------------------------

# 7. Write a Python Program to calculate the root of a Quadratic Equation. 
# Test Data : 1 5 7
# Expected Output :
# Root are imaginary;

#--------------------------------------------------------------------------------

# 8. Write a Python Program to read roll no, name and marks of three subjects and calculate the total, percentage and division. 
# Test Data :
# Input the Roll Number of the student :784
# Input the Name of the Student :James
# Input the marks of Physics, Chemistry and Computer Application : 70 80 90
# Expected Output :
# Roll No : 784
# Name of Student : James
# Marks in Physics : 70
# Marks in Chemistry : 80
# Marks in Computer Application : 90
# Total Marks = 240
# Percentage = 80.00
# Division = First

# roll_no=(input("Input the Roll Number of the student : "))
# name=input("Input the Name of the Student : ")

# phy, chem, ca = map(int, input("Input the marks of Physics, Chemistry and Computer Application : ").split())

# total=phy+chem+ca

# percent= float(total/300)*100

# print("Roll No : ",roll_no)
# print("Name of Student : ", name)
# print("Marks in Physics : ", phy)
# print("Marks in Chemistry : ", chem)
# print("Marks in Computer Application : ", ca)
# print("Marks in Percentage : ", percent,"%")

# if percent>=60:
#     print("Division = First")
# elif percent<=50 and percent>60:
#     print("Division = Second")
# elif percent<=33 and percent>50:
#     print("Division = Thired")
# else:
#     print("No division awarded")


#------------------------------------------------------------
# 9. Write a Python Program to read temperature in centigrade and display a suitable message according to temperature state below : 
# Temp < 0 then Freezing weather
# Temp 0-10 then Very Cold weather
# Temp 10-20 then Cold weather
# Temp 20-30 then Normal in Temp
# Temp 30-40 then Its Hot
# Temp >=40 then Its Very Hot
# Temp >=40 then Its Burning

# temp=int(input("Enter temperature: "))

# if temp<=0:
#     print("Weather is frezing")
# elif temp>=1 and temp<=10:
#     print("Weather is very cold")
# elif temp>10 and temp<=20:
#     print("Weather is cold")
# elif temp>20 and temp<=30:
#     print("Weather is Normal")
# elif temp>30 and temp<=40:
#     print("Weather is hot")
# elif temp>40 and temp<=50:
#     print("Weather is very hot")
# else:
#     print("Weather is burning")

#------------------------------------------------------------


# 10. Write a Python Program to check whether a triangle is Equilateral, Isosceles or Scalene. 
# Test Data :
# 50 50 60
# Expected Output :
# This is an isosceles triangle.
# 1.	Equilateral Triangle:
# •	All three sides are of equal length.
# •	All three angles are also equal, each measuring 60 degrees.
# 2.	Isosceles Triangle:
# •	At least two sides are of equal length.
# •	The angles opposite the equal sides are also equal.
# 3.	Scalene Triangle:
# •	All three sides have different lengths.
# •	None of the angles are equal.

# s1=(int(input("Enter the length of first side: ")))
# s2=(int(input("Enter the length of second side: ")))
# s3=(int(input("Enter the length of third side: ")))

# if s1<=0 or s2<=0 or s3<=0:
#     print('All sides length should be in positive ')
# elif s1+s2<=s3 or s1+s3<=s2 or s2+s3<=s1:
#     print("Invalid length: The sum of any two sides must be greater than the third side.")
# elif s1==s2==s3:
#     print("The triangle is Equilateral")
# elif s1==s2 or s1==s3 or s2==s3:
#     print("The triangle is Isosceles")
# else:
#     print("The triangle is Scalene")

#----------------------------------------------------------

# 11. Write a Python Program to check whether a triangle can be formed by the given value for the angles. 
# Test Data :
# 40 55 65
# Expected Output :
# The triangle is not valid.

# a1=(int(input("Enter first angle of triangle: ")))
# a2=(int(input("Enter second angle of triangle: ")))
# a3=(int(input("Enter third angle of triangle: ")))

# if a1+a2+a3==180:
#     print("The triangle is valid")
# else:
#     print("The triangle is not valid")

#-----------------------------------------------------------------------------------

# 13. Write a Python Program to check whether an alphabet is a vowel or consonant. 
# Test Data :
# k
# Expected Output :
# The alphabet is a consonant.

# alpha=(input("Enter an alphabet: "))
# v=['a','e','i','o','u', 'A','E','I','O','U']

# if alpha in v:
#     print("The alphabet is a vovel")
# elif alpha.isalpha():
#     print("The alphabet is a consonant")
# else:
#     print("Invalid input. Please enter a single alphabet.")