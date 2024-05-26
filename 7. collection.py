## Collection is a data type to collect multiple data

    # Type of collection
        # List
        # Tuple
        # set
        # dict

##  list 

    # list stores any type of data
    # list is an index collection
    # list is a mutable (changable) collection
    # data can be repeted in list
    # we can make copy of list

l=[23,5.6,5+7j,"python",[43,"ducat",4.3],"python",5.6]
# print(l)

# print(len(l))

## indexing

# print(l[0])
# print(l[-1])
# print(l[-3][1])

## slicing

# print(l[1:-2])

## revers

# print(l[::-1])


# l=[23,5.6,5+7j,"python",[43,"ducat",4.3],"python",5.6]

## iteration (loop)

# for i in l:
#     print(i)

# for i in l[-3]:
#     print(i)

## pre defined function

# max function- give max value in list, data type should be same
# l=[1,4,6,8,9,12.9,5,2,6,100,1]
# print(max(l))
# print(min(l))
# print(sum(l))
# print(sorted(l)) # Sort with value [1, 1, 2, 4, 5, 6, 6, 8, 9, 12.9, 100]
# print(sorted(l,reverse=True)) # reversed with value [100, 12.9, 9, 8, 6, 6, 5, 4, 2, 1, 1]
# print(list(reversed(l))) # reversed with index number [1, 100, 6, 2, 5, 12.9, 9, 8, 6, 4, 1]


# Methods

l=[23,5.6,5+7j,"python",[43,"ducat",4.3],"python",5.6]
# l.append(75) # insert data at last
# l[-3].append(34)

# l.insert(3,75) # insert data in between

# l.extend([1,2,3,4,5]) # insert multiple data

# l.remove('python') # remove data wise

# l.pop(2) # remove on the bases of index

# l.clear() # to clear whole list

# l1=l.copy()

# l.clear()

# print(l)
# print(l1)


# l=[23,5.6,5+7j,"python",[43,"ducat",4.3],"python",5.6]

# print(l.count("python")) # count how many times a data is in the list ## output 2

# print(l.index(5+7j)) # this will return the index value of a particular data ## output 2

# print(l.index(5+7j,3)) # this will count if value repert after first index ## output error, bcoz only once

# l.reverse() # will reverse the value in list

# print(l)

#### create empty list

# l1=[]
# l2=list() ## This is use to typecast value (eg change tuple to list)

# print(l1)
# print(l2)



#------------------------------------------------------------------------------------------

# Q and A

# 1. Write a Python program to sum all the items in a list. 

# l=[1,4,6,8,9,12.9,5,2,6,100,1]

# print(sum(l))



# 2. Write a Python program to multiplies all the items in a list. 

# l=[1,2,3,4,5,6]
# i=1
# m=1
# while i<=len(l):
#     m=m*i
#     i+=1
# print("multiplaction",m)


# l=[1,2,3,4,5,6]
# i=1
# m=1
# for i in l:
#     m=m*i
# print("multiplaction",m)



# 3. Write a Python program to get the largest number from a list. 

# l=[1,4,6,8,9,12.9,5,2,6,100,1]

# print(max(l))

# a=0

# for i in l:
#     if i>a:
#         a=i
# print(a)

#--------------------------------------------------------------------------------

# 4. Write a Python program to get the smallest number from a list. 

# l=[1,4,6,8,9,12.9,5,2,6,100,1]

# print(min(l))

#-----------------------------------------------------------------------------

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

# l=['abc', 'xyz', 'aba', '1221']
# c=0
# for i in l:
#     if len(i)>=2:
#         if i[0]==i[-1]:
#             c+=1
# print(c)

#----------------------------------------------------------------------------------------------------

# 6. Write a Python program to remove duplicates from a list. 

# l=[23,5.6,5+7j,"python",[43,"ducat",4.3],"python",5.6]
# ul=[]
# for i in l:
#     if  i not in ul:
#         ul.append(i)

# print(ul)

## squre of each value in the list and store it in new list

# l=[1,2,3,4,5]

# l1=[]

# i=1

# for i in l:
#     l1.append(i**2)
# print (l1)

## get unique data in list [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5]

# l=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,5]

# l1=[]

# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

##------------------------------------------------------------------------------------


## 9. Write a Python program to find the list of words that are longer than n from a given list of words. 

# x=int(input("Enter a length: "))

# l=['java','python','java script','php','dotnet']

# l1=[]
# for i in l:
#     if len(i)>=x:
#         l1.append(i)
# print(l1)

##------------------------------------------------------------------------------------------------


## 10. Write a Python function that takes two lists and returns True if they have at least one common member. 



# def com(l1, l2):
#     for i in l1:
#         if i in l2:
#             return True       
#     return False


# l1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# l2=['Green', 'White', 'Black']

# print(com(l1,l2))

# def has_common_member(list1, list2):
#     for item in list1:
#         if item in list2:
#             return True
#     return False

# # Example usage:
# list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# list2 = ['Green', 'White', 'Black']
# print(has_common_member(list1, list2))  # Output: Tru



# 11. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# l= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# index=[0,4,5]

# for i in sorted(index,reverse=True):
#     l.pop(i)

# print(l)


#--------------------------------------------------------------------------------

# 12. Write a Python program to generate a 3*4*6 3D array whose each element is *. 

# Array is a collection of same elements

# [1,2,3,4,5,6]

# [1,2,3,4]

# ['*','*','*','*','*'] # 1 D example it has 5 element

# 1D- have a length or a width

# 2D - is a collection of 1D, it has both length and breath

# [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']] - it has 4 rows and each rows has 5 element (4,5)

# 3D - is a collectio of 2D

# [['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],
#  ['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']
 
#  ['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*'],['*','*','*','*','*']] (3,4,5)

# It has LXBXH

# l1=[]
# l2=[]
# l3=[]
# for k in range(3):
#     for j in range(4):
#         for i in range(6):
#             l1.append('*')
#         l2.append(l1)
#     l3.append(l2)    
# print(l2)

#----------------------------------------------------------------------------------------------


# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# l=[1,2,3,4,5,6,7,8,9]

# l1=[]

# for i in l:
#     if i%2!=0:
#         l1.append(i)
# print(l1)


#--------------------------------------------------------------------------------------------------

# 14. Write a Python program to shuffle and print a specified list. 



# 21. Write a Python program to flatten a shallow list. 

# l1=[[1,2],[3,4],[5,6,7]]
# l2=[]

# print(sum(l1,l2))




## 30. Write a Python program to check whether a list contains a sublist. 

 












####-----------------------------===================-------------------------

# Tuple
    # Tuple stores any type of data
    # Tuple is an index collection
    # Tuple is a immutable (cannot be changed) collection
    # data can be repeted in tuple
    # we cannot make copy of tuple

# t=(2,"python",3.6,[3.4,"ducat"])

# print(t)
# print(len(t))

# print(t[2])

## Slicing

# print(t[2 :]) ## output (3.6, [3.4, 'ducat'])
# print(t[:2]) ## output (2, 'python')


## data integration

# for i in t:
#     print(i)

# print(t.count(2)) ## count how many time a data has come

# print(t.index(2)) ## index value of data in tuple

## function

# t=(91,2,44,55,6,7,89)

# print(max(t))
# print(min(t))
# print(sum(t))
# print(sorted(t))
# print(tuple(reversed(t)))


## Packing and unpacking

# t=1,2,3,4,5,6  ## this is called packing data in tuple (it will be by default considered as tuple)

a,b,c=1,2,3 ## this is called packing tuple data (each variable will contain one value)


### Typecast - use to insert value in tuple

# t=(91,2,44,55,6,7,89)

# l=list(t)

# l.append (47)

# t=tuple(l)

# print(t)


##---------------------------------------------------------------


# Set 
    # Set stores any type of data except for mutable data (collection like list, it s also know as the data can be changed) we can put tuple in this
    # set is an unindex collection
    # set is a mutable (can be changed) collection
    # data cannot be repeted in set
    # we can make copy of set

# s={23,5.6,5+7j,"python",(43,"ducat",4.3),"python",5.6}

# print(s)  ## {(43, 'ducat', 4.3), 'python', 5.6, 23, (5+7j)}

# print(len(s)) ## 5

# s={91,2,44,55,6,7,89}

# print(max(s))
# print(min(s))
# print(sorted(s))
# print(sum(s))

# for i in s:
#     print(i)


# s={91,2,44,55,6,7,89}

# for i in s:
#     print(i)

# Set method

# s={91,2,44,55,6,7,89}

# print(s)

# s.add("ducat") ## need to add single eliment ## 

# s.update([1,5,9,21,67]) ## need to add multiple eliments  ##  {1, 2, 67, 5, 6, 7, 9, 21, 89, 91, 44, 55}

# s.remove(91) ## remove data ## {2, 55, 6, 7, 89, 44}, it will give error in non excisting data

# s.discard(91) ## remove data ## {2, 55, 6, 7, 89, 44}, it will not give error in non excisting data

# s.pop()
# s.clear()

# s1=s.copy()

# s1={'a','b','c','d'}
# s2= {'e','a','f','g'}

# print(s1.intersection(s2)) # commen element between s1 and s2

# print(s1.union(s2)) # joint both s1 and s2

# print(s1.difference(s2)) # different between both set

# print(s1.symmetric_difference(s2))


# print(s1)

# s1={'a','b','c','d'}
# s2= {'a','b'}

# print(s1.issuperset(s2))

# print(s2.issubset(s1))

# s1={'a','b','c','d'}
# s2= {'a','f'}

# print(s1.isdisjoint(s2)) ## true if there is no commom element, false if there is a common element

# s1={'a','b','c','d'}
# s2= {'a','b'}




##------------------------------------------------------------------------------------------------

## Dictionary
            # we store data in {key:value} format
            # Keys are made with Primitive type of data
            # Value can be of any type
            # Dic is an index collection . Indexing is done on the bases of Keys    
            # Dic is a mutable (can be changed) collection
            # value can be repeted in this, but key value is not been repeted (as it will overide the value). 
            # Dic can be copied

# d={1:"python",'a':"Apple", 'aman':23,'name':['Rohit', 'Rahul', 'Arjun', 'Ankit']}

# print(d)
# print(len(d))

#indexing

# print(d['a'])  ## Apple
# print(d['name']) ## ['Rohit', 'Rahul', 'Arjun', 'Ankit']

# print(d[1]) # python

## there is no concept of slasing in dic

## Loop (iteration)

# for i in d:
    # print(i) ## Will Iterate key
    #output
    # 1
    # a
    # aman
    # name

    # print(d[i]) ## will Iterate value in key 
    #output
    #python
    # Apple
    # 23
    # ['Rohit', 'Rahul', 'Arjun', 'Ankit']


# d={1:"python",'a':"Apple", 'aman':23,'name':['Rohit', 'Rahul', 'Arjun', 'Ankit']}

# Add a data

# d[b]= 'ant'

# print (d)

# d={1:'a',2:'b',4:'c',3:'d'}

# Function

# all below function will give Key as the output
# print(max(d)) # 4
# print(min(d)) # 1
# print(sum(d)) #10
# print(sorted(d)) # [1, 2, 3, 4]
# print(list(reversed(d))) # [3, 4, 2, 1]

# all below function will give value as the output
# print(max(d.values())) # d
# print(min(d.values())) # a
# print(sorted(d.values())) # ['a', 'b', 'c', 'd']
# print(list(reversed(d.values()))) # ['d', 'c', 'b', 'a']


# method

# d={1:"python",'a':"Apple", 'aman':23,'name':['Rohit', 'Rahul', 'Arjun', 'Ankit']}

# print(d.values()) # dict_values(['python', 'Apple', 23, ['Rohit', 'Rahul', 'Arjun', 'Ankit']])
# print(d.keys()) # dict_keys([1, 'a', 'aman', 'name'])
# print(d.items()) ## this will give zip format data # dict_items([(1, 'python'), ('a', 'Apple'), ('aman', 23), ('name', ['Rohit', 'Rahul', 'Arjun', 'Ankit'])])

# d.setdefault('c',"cat") ## {1: 'python', 'a': 'Apple', 'aman': 23, 'name': ['Rohit', 'Rahul', 'Arjun', 'Ankit'], 'c': 'cat'}
# d.setdefault('c') # if there is no value it will pass none ## {1: 'python', 'a': 'Apple', 'aman': 23, 'name': ['Rohit', 'Rahul', 'Arjun', 'Ankit'], 'c': None}
# print(d)

# print(d.get('a')) ## Apple

# d.update({'d':'ducat','p':'python'}) # add the data  ## {1: 'python', 'a': 'Apple', 'aman': 23, 'name': ['Rohit', 'Rahul', 'Arjun', 'Ankit'], 'd': 'ducat', 'p': 'python'}

# d.pop('a') # remove the data  ### {1: 'python', 'aman': 23, 'name': ['Rohit', 'Rahul', 'Arjun', 'Ankit']}

# d.popitem() # this will remove last item  ## {1: 'python', 'a': 'Apple', 'aman': 23}

# d.clear() # remove all the data in dic.

# print(d)

# d1=d.copy()

# print(d1)

# l=[1,2,3,4,5]

# d={}

# d=d.fromkeys(l)

# print(d) ## {1: None, 2: None, 3: None, 4: None, 5: None}


# 1. Write a Python script to sort (ascending and descending) a dictionary by value. 


#------------------------------------------------------------------------------------------


## List comprehension - Changes needs to be done in same list

# l=[1,2,3,4,5]

# old method
# l1=[]

# for i in l:
#     l1.append(i**2)
# print(l1)

# l=[i**2  for i in l]

# print(l)

# if we need to squar only few value in list

# l=[i**2 for i in l if i<=3]

# print(l)

# l=[i**2 if i<=3 else i**3 for i in l]

# print(l)

# l=[[1,2,3,],[4,5,6],[7,8,9]]

# l= [j**2 for i in l for j in i]

# print(l)

# l=[[j**2  for j in i]  for i in l ]

# print(l)

# l=[[['*' for k in range(6)]for k in range(6)]for i in range(3)]

# print(l)

# Dictionary comprehension

# d={i:i**2   for i in range(1,16)}
# print(d)


# d={i:i**2 if i<=7 else i**3 for i in range(1,16) }
# print(d)

# make list to set

# l=[1,2,3,4,5]

# s={i**2 for i in l}

# print (s)