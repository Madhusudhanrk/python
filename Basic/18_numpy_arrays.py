# #INTRO TO numpy Arrays **********************************************************************
from numpy import *

arr = array([1,2,3,4])#no need to mention array type
arr = arr + 5 # value has been added every element in array
print(arr)#o/p [6789]

arr1 = array([1,2,3,4])

arr = arr+arr1# two arrays added

print(arr)#o/p [7 9 11 13]

#methods and function in numpy

arr = sqrt(arr)#[7 9 11 13] values, can use min(),max()
print(arr)#o/p [2.64575131 3.         3.31662479 3.60555128] 

arr1 = array([1,2,3,4])
arr2 = array([0,2,3,4])

arr = concatenate([arr1,arr2])
print(arr)#o/p [1 2 3 4 0 2 3 4]

#copying array 2 types
"""
1.shalow copy  => different id, but value changed in original array copied array value also effected
2.deep copy    => different id, no connection
"""
arr1 = array([1,2,3,4])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))#if we assign it copy values but id remain same
print(id(arr2))

arr2 = arr1.view()#if we change value it effect copied array also shalow copy
print(arr2)
print(id(arr1))
print(id(arr2))

arr2 = arr1.copy()#two separated deep copy
print(arr2)
print(id(arr1))
print(id(arr2))

