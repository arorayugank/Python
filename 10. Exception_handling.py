## Exception handling- Errors are called exception

## Syntax Error are not considered in exception handling

## Exception are those error which comes after exequation of program (Run time Error)

## try block is used for exception handling, we write excpet block aling with try

## try block is used where the data has been outsorced or requested form user 

# try:
#     i=int(input("Enter a number: "))
#     print(i)
# except:
#     print("Intiger no. is accepted only")
# print("Done")

## Diffrent types of error handling

# try:
#     i=int(input("Enter first number: "))
#     j=int(input("Enter second number: "))
#     print("Division: ",i/j)
# except ValueError:
#     print("Intiger number is accepted only")
# except ZeroDivisionError:
#     print("Division by zero is invalid")
# print("Done")

# if we don't know the type of error we use unknown error

# try:
#     i=int(input("Enter first number: "))
#     j=int(input("Enter second number: "))
#     print("Division: ",i/j)
# except ValueError:
#     print("Intiger number is accepted only")
# except ZeroDivisionError:
#     print("Division by zero is invalid")
# except:
#     print("unknown error")
# print("Done")


# if we want to show or raise the error- we use raise keyword for this (this is programer defined error)

# age=int(input("Enter the age: "))

# if age>=18:
#     print("Ok")
# else:
#     raise ValueError("Age must be 18+") ## We have raised the error here

#-------------------------------------------------------------------------------------------------

## user defined exception 

# class AgeError (Exception):
#     pass
# age=int(input("Enter the age: "))

# if age>=18:
#     print("Ok")
# else:
#     raise AgeError("Age must be 18+")
