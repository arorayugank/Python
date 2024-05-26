## File Handling

## File is a collection of generic data

## Type of file:
        # Text file -- notepad, word, PDF,excel
        # Binary file - exe, image file (JPEG, PNG), bin, bat, MPEG,MKV

## File handling - is use to store the data (input or output data) to get it for a program.
    # Read - to read the data form a file  -- r
    # Write - to add the data to the file  -- W
    # append - to change the data in a file-- a
    # create - to create a file -- x 

# if file in within the folder whre we arwe accessing we have to just mention file name with extension

# f=open("1. First.py", mode='r')

# print(f.read())

# if the file is in different directory

# a=open('C:\Users\Disha\Desktop\hello_python.txt') # \ will not work in python as it is a predifined code as \n

# first alternate
# a=open('C:/Users/Disha/Desktop/hello_python.txt')
# second alternate
# a=open('C:\\Users\\Disha\\Desktop\\hello_python.txt')
# Third alternate
# a=open(r'C:\Users\Disha\Desktop\hello_python.txt', mode='r') # r means raw text, this is the most common methord
# print(a.read())

# if we want to read ther data till a length
# in this if first 5 character are read then it will read next 5 char.

# print(a.read(5))
# print(a.read(5)) 

# readline - we use this to read one line at a time.

# print(a.readline())

# readlines - will give all the lines in one list

# print(a.readlines())  #['Hello, I am first program of python\n', 'I am simple\n', 'I have functions']

#-------------------------------------------------------------------------------------

## Write mode

# if you open a file in write mode, if there is no file the it will create a new file.
# if file is already there then it will override the data (remove previous data and add the new data mention in the program)

a=open(r'C:\Users\Disha\Desktop\hello_python.txt', mode='w')
a.write("I do programming for DS\nI do programming for ML")

#--------------------------------------------------------------------------------------------

## Apend mode - 

# if you open a file in append mode, if there is no file the it will create a new file.
# it will add new data in exting data

# a=open(r'C:\Users\Disha\Desktop\hello_python.txt', mode='a')
# a.write("\nI am Python")

#----------------------------------------------------------------------------------------------

# create mode - use to create a new file, it can be used only once

# a=open(r'C:\Users\Disha\Desktop\python.txt', mode='x')
# a.write("I am Python")


#-------------------------------------------------------------------------------------------------

# Binary format - is use to see the data in binary format  

# a=open(r'C:\Users\Disha\Desktop\hello_python.txt', mode='rb')

# print(a.read())


#--------------------------------------------------------------------------------------------------

# Removal of file

# import os

# os.remove(r"C:\Users\Disha\Desktop\python.txt")

# print(os.path.exists(r"C:\Users\Disha\Desktop\python.txt"))

# print(os.mkdir("python")) # use to create a directory

# os.rmdir("python") # use to remove a directory

