#INTRO TO input **********************************************************************

# x = int(input("Enter a number and find square of it:\n"))# input returns string
# x = x//2 #flooer
# print(x)

# x = int(eval(input("Enter a expression:\n")))# eval expression


# x = input("Enter first char of ur name:\n")[0]# limit only 1 char
# print(x)  


import sys
x = int(sys.argv[1]) # [0] is file name start from 1 index, Pass argument value while running
print(x)  