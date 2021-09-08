#DATA TYPES in Python
"""
1. None -> Null in other languages ""
2. Numeric-> Int, Float, Complex, Bool
"""
"""
ALL ARE SEQUENCE DATA TYPES 1 BY 1

3. List    -> a = []
4. Tuple   -> a = ()
5. Set     -> a = {}
6. Range   -> range(start,stop,steps)
7. Strings -> "text"

"""
"""
8. Dictionary -> a = {'key':'value'} Map in other languages
"""

# None***********

a = "" #no value assigned so it is None or null
print(a)

#Numeric**********
a = 5
print(type(a)) # INT type value 5

a = float(5)
print(type(a)) # FLOAT type value 5.0

a = complex(5,6) # complex(val1,val2*j)
print(type(a)) # COMPLEX type 
print(a) # value 5+6j

#BOOL**********

print(6>7) # o/p False

print(int(True)) # o/p 1 TRUE = 1, False = 0 if type converted to numeric

# SEQUENCE DATA TYPES (ONLY ABOUT RANGE EXCEPT WILL BE DISCUSSED DETAILED)


# RANGE********* 

# syntax range(start,stop,steps) and stop-1 because range starts from 0 like arrays

a = list(range(0,10)) # range return range object so converting to list
print(a) # 0 to 9 because it like array start from 0
a = list(range(0,10,2)) # skip 2-1=> 1 step 
print(a)


#DICTIONARY detailed explained


