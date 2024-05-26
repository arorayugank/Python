# Regular Experssion - it is used to generate pattern for string data

# this is used to check and extract the data form another data

# it is also used to get correct data  in a doc, or want to extraxt mobile no. which are correct, or email Id which is correct 

# normal codding
# s="PYTHON is best programing language"

# if "python" in s:
#     print("Found")
# else:
#     print("Not Found")

# Regular Experssion

# import re

# s="PYTHON is best programing language"

# if re.search("[pP][yY][tT][hH][oO][nN]",s):
#     print("Found")
# else:
#     print("Not Found")

# match=re.match("[pP][yY][tT][hH][oO][nN]",s)

# print(match.span()) # will show the index no. # output is (0,6)



# s="Amit is 25.Akash is 22, Ankit is 26, Aman is 21"

# one way

# data=re.findall("[0-9]",s) #[] is used to match char by char and retun according to char, # output is ['2', '5', '2', '2', '2', '6', '2', '1']

# another way

# data=re.findall("[0-9]{2}",s) # output ['25', '22', '26', '21']

## another way

# s="Amit is 25, Akash is 22, Ankit is 26, Sumit is 2134"


# data=re.findall("[0-9]{1,4}",s)  # output is ['25', '22', '26', '2134']
# print(data)

# data=re.findall("[A-Z][a-z]{1,10}",s) # output is ['Amit', 'Akash', 'Ankit', 'Sumit']

# data=re.findall("A...t",s) # output ['Ankit']

# data=re.findall("A.{1,10}t",s) # output is ['Amit', 'Ankit']

# data=re.findall("A...?",s) # output is ['Amit', 'Akas', 'Anki']

# Exclude the data - ^ symbole is used for exclusion

# data=re.findall("[^0-9]{2,6}",s)

# print(data)