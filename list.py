#INTRO TO LIST **********************************************************************

nums = [10,20,30,40,50]
print(nums)

nums = [10,'madhu',1.5,10]
print(nums)

""" 
Rule 1: List works on Index based 
Rule 2: List takes different types of values
"""

nums[1] = "madhusudhan"
print(nums)
nums =(nums,["madhusudhan"])
print(nums)

"""
Rule 3: List are Mutable and ordered by index
Rule 4: List allow Duplicate values
Rule 5: List Can hold any Datatypes like int,float,List,set,tuple,dict
"""

# PYTHON List supports Methods *********************************************************************

nums = [10,'madhu',1.5,10]
# ADD METHODS
nums.append(20) 
nums.insert(1,"me")
nums.extend([11,22,33])
print(nums)

"""
ADD METHODS

LIST.append => append(value) -> Add item at last of the list
LIST.insert => insert(index,value) -> Add item based on given index in the list
LIST.extend => extend(list[values]) -> Add list of items last in the list
"""

# REMOVE METHODS

# nums.remove(33)
# nums.pop()
# nums.pop(0)
# del nums[2:]
# print(nums)
# del nums

"""
REMOVE METHODS

LIST.remove => remove(value) -> Remove the given value in the list
LIST.pop => pop(),pop(index) -> Remove the last value or removes the index value if mentioned
LIST.del => del LIST, del LIST[INDEX] -> Remove the list based on name or value based on index number

"""
# Miscellaneous Methods
# nums = [10, 'me', 'madhu', 1.5, 10, 20, 11, 22, 33] FOR REFERENCE
nums.reverse()
n_count = nums.count(10)
nums.clear()
print(n_count)
print(nums)

"""
Miscellaneous METHODS

LIST.reverse => reverse() -> Reverse the origin List
LIST.count => count(value) -> This will count the value no of time present in the list
LIST.clear => clear() -> Clear entire list

"""
# PYTHON List supports Funtions *********************************************************************

digits = [11,2 2,33,44]
print(sum(digits))
print(min(digits))
print(max(digits))

"""
IN this only Numerics allowed
"""
print(digits[2:])# 0 counted 
print(digits[2:6])# higher index will be skipped
print(digits[:])# or [digits]
print(digits[:-3])# no 0 counted but -1 same
"""
LIST SLICE => [start:stop-1] -> If start,stop index neither not metioned it takes from first,last index
                                supports negative values but in reverse
"""
