#INTRO TO Filter,Map,Reduce *********************************************************************

from functools import reduce

"""
SYNTAX:
filter_object = filter(func,sequence) it returns filtered value in object form
"""
lst = [2,1,5,3,5,6,8,4]
filtered_obj = filter(lambda a : a%2==0,lst)
result = list(filtered_obj)
print(result)
# in filter if condition true only it return value if false it won't return
# and filter always expect conditions like filter out the values

lst = [2,1,5,3,5,6,8,4]
filtered_obj = map(lambda a : a%2==0,lst)
result = list(filtered_obj)
print(result)
# in Map if condition true or false everything will be returned based on what we return 
# and Map always expect conditions like evaluate the values

lst = [2,1,5,3,5,6,8,4]
reduced_values = reduce(lambda a,b : a+b,lst)
# reduce always try to reduce the output to single index value with two parameters
print(reduced_values)