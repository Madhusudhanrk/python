# 83. Write python function which takes a variable number of arguments.
# A function that takes variable arguments is called a function prototype. Syntax:

# For example:
# def function_name(*arg_list)

# def func(*var):
# #    print(type(var)) #tuple
#    for i in var:
#        print(i)
# func(1)
# func(20,1,6)

# The * in the function argument represents variable arguments in the function.


# 84. WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.
# You can do this by converting the list to set by using set() method and comparing the length of this set with the length of the original list. If found equal, return True.

# def check_distinct(data_list):
#  if len(data_list) == len(set(data_list)):
#    return True
#  else:
#    return False;
# print(check_distinct([1,6,5,8]))     #Prints True
# print(check_distinct([2,2,5,5,7,8])) #Prints False


# 85. Write a program for counting the number of every character of a given text file.
# The idea is to use collections and pprint module as shown below:

# import collections
# import pprint
# with open("sample_file.txt", 'r') as data:
#  count_data = collections.Counter(data.read().upper())
# #  print(count_data)
#  count_value = pprint.pformat(count_data)
#  print(count_value)

#  87. Write a Program to add two integers >0 without using the plus operator.
# We can use bitwise operators to achieve this.

# def add_nums(num1,num2):
#     while num2 !=0:
#         data = num1 & num2
#         num1 = num1 ^ num2
#         num2 = data<<1
#     return num1

# print(add_nums(2,3))


# 88. Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:
# ax + by = c
# mx + ny = o
# By solving the equation, we get:

# a, b, c, m, n, o = 5, 9, 4, 7, 9, 4
# temp = a*n - b*m
# if n != 0:
#    x = (c*n - b*o) / temp
#    y = (a*o - m*c) / temp
#    print(str(x), str(y))

# 90. Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.
# We can again use the re module to convert the date string as shown below:
 

# from datetime import datetime

# newformat = datetime.strptime("1998-07-15","%Y-%m-%d").strftime("%d-%m-%Y")
# print(newformat)

# 91. Write a Program to combine two different dictionaries. While combining, if you find the same keys, you can add the values of these same keys. Output the new dictionary
# We can use the Counter method from the collections module

# from collections import Counter
# d1 = {'key1': 50, 'key2': 100, 'key3':200}
# d2 = {'key1': 200, 'key2': 100, 'key4':300}
# # print(Counter(d1))
# new_dict = Counter(d1) + Counter(d2)
# print(new_dict)

#  92. How will you access the dataset of a publicly shared spreadsheet in CSV format stored in Google Drive?
# https://docs.python.org/3/We can use the StringIO module from the io module to read from the Google Drive link and then we can use the pandas library using the obtained data source.

# from io import StringIO
# import pandas as pd
# csv_link = "https://docs.google.com/spreadsheets/d/..."
# data_source = StringIO.StringIO(requests.get(csv_link).content))
# dataframe = pd.read_csv(data_source)
# print(dataframe.head())