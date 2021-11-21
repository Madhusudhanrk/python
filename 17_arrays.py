# #INTRO TO Arrays **********************************************************************
# import array as arr
# a = arr.array("i",[1,2,3])
# print(a)  # first method to work with arrays

# """
# b = signed char     -> 1 byte
# B = unsigned char   -> 1 byte
# u = unicode char    -> 2 byte
# h = signed short    -> 2 byte
# H = unsigned short  -> 2 byte
# i = signed integer  -> 2 byte
# I = usigned integer -> 2 byte
# l = signed long     -> 4 byte
# L = usigned long    -> 4 byte
# f = signed float    -> 4 byte
# d = usigned double  -> 8 byte
# """

# from array import *

# val = array("i",[1,-2,3,4])
# print(val)#o/p array('i', [1,-2, 3, 4]) it is signed int it accept values negative


# val = array("I",[1,-2,3,4])
# print(val)#o/p erro unsigned int can't accept negative values

# # Array methods and funtions*******************************************
# arr_type = val.typecode
# print(arr_type)#o/p array type

# arr_info = val.buffer_info()
# print(arr_info)#o/p (1539155313296, 4) address, array size

# val = array("i",[1,-2,3,4])
# val.reverse()# return none but values reversed
# print(val)#o/p array reverse


# #Array and loop combine
# val = array("i",[1,-2,3,4])

# newarr = array(val.typecode, (a for a in val))

# for i in newarr:
#     print(i)

# adding values to array dynamically
# import array #for methods arr.array
# from array import * #for fucntions
# count = int(input('how many values to be added:'))
# arr = array('i',[])
# for i in range(0,count):
#     val = int(input('enter value:'))
#     arr.append(val)
# print(arr)

#finding index of the value in array

# value = int(input('Enter value we will finde index:'))
# k = 0
# for e in arr:
#     if e == value:
#         break
#     k +=1
# print('index is:',k)

# print(arr.index(value))


