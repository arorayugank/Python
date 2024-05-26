
# type of data

# 1. Primitive Type - define individul property (eg: Gender)
        # numeric data
                # int- non decimil data
                # Float - decimil data (fraction data)
                # Complex - static and dinamic number
        # text
                # str- use to store string data
        # boolen
                # bool - use to store 'True', 'False' input
        # bytes
                # bytes: to store binery data
        # none type
                # nonetype- store nont type diffiend data


# 2. non primitive type - define collative property (eg: Nationility), also known as collection type

        # List
        # tuple
        # range
        # Set
        # frozenset
        # dict (dictionary)
        # bytearray


#----------------------------------------------------------
# Type- This function is use to identify type of data

# i=12334.7
# print (type(i))

# i=6+8j # complax no. example
# print(type(i))


# s= 'python'
# S1="Java"

# print(type (s))
# print(type (S1))


# i=None
# print(type (i))




#------------------------------------------------------------
# # list - collection of all types of data, but in [] braket

#     list assign index no. to each value
#     exp - 2 has index value of 0, python has index value of 1 and so on
# We can change the data of any index

# l=[2,'python',8.3, 7+8j,True]

# print(type (l))

# print (l[0])


#------------------------------------------------------------

# Tuple - collection of all types of data but in () braket

# it Also assign index number
# We cannot change the data in this

# t=(2,'python',8.3, 7+8j,True)

# print(type (t))

# print (t[3])



#-----------------------------------------------------------
# Range - is a collection on integer (number), but in sequence (assending or disending)
# need to mention one +1 value at end value

# text range(start value, end value + 1, range)

# if no range then range is 1

# if no start value the it is 0

# to print the range text is print(list(r))

# We cannot change data

# r=range(1,101,1)

# print(list(r))

# r1 = range(100,0,-1)
# print(list(r1))

# print(r[3])

#----------------------------------------------------------------------------------------------------

# Set - data will be stored in {} bracked, and can be of any type

# it do not have index, and it can print in any sequence

# and it cannot access repet data eg (1,2,3,4,1) 1 will not repet in output

# We can add and remove data

# s= {2,'python',8.3, 7+8j,True}

# s.add(45)

# s.remove(8.3)

# print(type (s))

# print(s)

#-----------------------------------------------------------------------------------------

# frozenset- is also a verson of set, but we cannot add and remove data in this 

# we have to create a set and then we can use frozenset on it

# fs=frozenset(s)

# print(fs)

#-----------------------------------------------------------------------------------

# dict (dictionary) - index is called key and data is called value, it is made in {}

# key cannot be repeted

# we can add and remove data in this

# # d= {1:'python','a':'apple'}

# # print(d)

# # print(d[1])

# # d['a'] = "computer"


# # print(d)

#-------------------------------------------------------------------------------------
# Bytearray- is use to change the value of charater in string, with the help of Ascii code

# s='python'

# s1=b'python'

# ba=bytearray(s1)

# ba[1]=112

# print(ba)
# print(s[2])

# print(s1 [2])


# -----------------nxt topic-----------------------


# Type converson or type casting

# it is use to cange the type of value (but value will remain same)


# x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 - this is Null character

# Base value - no. of data use a value(data = number)

# Decimal - 10 (0 to 9)


# i=10

# print(float(i))
# print(complex(i))
# print(bool(i))
# print(str(i))
# print(bytes(10))

# j= 5.5
# print(int(j))
# print(complex(j))
# print(bool(j))
# print(str(j))

# k=4+5j

# print(int(k))
# print (float(k))
# print(bool(k))
# print (str(k))

# s="Yug"
# s1 = '123'

# print(int(s1))


# ASCII value

# print(ord('g'))

# print (chr(67))
