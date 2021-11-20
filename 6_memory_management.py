#INTRO TO python Memory management **********************************************************************
"""
IN python variables has same values they point to single address where first orgin value created

IN python values has address like id(10)->78555552=>a,b like we can tage variables to the value and its address

If value not used means it will be collected by garbage collection.
"""
x = 10
print(type(x)) #Type int

y = x

print(id(x)) #2668298109456
print(id(y)) #2668298109456

"""
y is empty now y=x means y=10
now x is 10
    y is 10

    x id is 2430817993232
    y is pointing to x id because of same value

"""
print(x) #10
print(y) #10

#now x value changed so address changed
x = x + 1 
print(x) #11
print(id(x))#2668298109488

#now y value not changed so address not changed
print(y) #10
print(id(y))#2668298109456

#now let's change y value

y=x
print(id(x)) #2443148657200
print(id(y)) #2443148657200



