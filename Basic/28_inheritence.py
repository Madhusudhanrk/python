class A():
    def feature1():
        print("feature 1")

class B():
     def feature2():
        print("feature 2")

class C():   
    def feature3():
        print("feature 3")

"""
if class B(A) ->single level inheritance
if class C(B) ->Multi level inheritance
if class C(A,B) ->Multiple Inheritance
"""

"""
if inherit class single level or any level if the obj created class has __init__ it will call it
if need to Use super class __init__ use super().__init__() add inside it's own __init__ inherited class
__inhit__ added.
in multiple inheritance it uses MRO method resolution order left to right only pick one
"""