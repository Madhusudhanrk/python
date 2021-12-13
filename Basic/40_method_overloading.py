"""
operator overloading -> means we can't add two objects like s1+s2 because the + __add() doesn't have adding 
                        method in __add()class or func we need to write custorm code.
if + operator doesn't support we need to create one supporting odd operands like class obj
"""

"""
method overloading -> simple if method overloading means if method taking 3 parameters passing only two values
"""


# method overriding

"""
method overriding means if A class has a method check() and B class also has method Check() and B class inherited A class.
If we call B calss check it will call only B class check not A class check this is method overriding

if two classes has same method when calling it prefer only which class we called.

"""
class father:
    def phone(self):
        print("Has samsung phone")

class son(father):
    def phone(self):
        print("Has iphone")

obj = son()
obj.phone()
