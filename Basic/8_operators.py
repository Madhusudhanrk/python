#INTRO TO Operators **********************************************************************

# 5 Types of Operators

"""
1. Artimetic operators
2. Logical operators
3. Relational operators
4. Assignment operators
5. Unary operators

"""

#1. Artimetic operators

a,b = 2,3
x = a+b
print("Artimetic")
print(x)#o/p->5  same for -,*,/,%

#2. Logical operators

a,b = 2,3
x = a==b
print("Logical")
print(x)#o/p->False   

x = a>b
print(x)#o/p->False 

x = a<b
print(x)#o/p->True

x = a<=b
print(x)#o/p->True 

x = a>=b
print(x)#o/p->False 

x = a!=b
print(x)#o/p->True 

#3. Relational operators

a,b = 2,3
x = a>b and a==b
print("Relational")
print(x)#o/p->False 

x = a>b or a==b
print(x)#o/p->False 

x = not a>b 
print(x)#o/p->True 

#4. Assignment operators

a,b = 2,3
print("Assignment")
print(a,b)#o/p->2 3

a += 5  # a= a + 5 same for -,*,/
print(x)#o/p->7

#5. Unary operators

a=5
print("Unary")
print(a)#o/p->5
print(-a)#o/p->-5



