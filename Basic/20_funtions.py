# #INTRO TO functions **********************************************************************

def update(a):
    a = 8
    print("inside Func",a)
a=10
update(a)
print("outside func",a)
#this example uses call by value not by reference there is no reference concept in python
#because python uses value address so value same no new address created

"""
Integers are immutable 
strings are immutable
but like list we can update
"""


#variable lenght arguments and keyworded variable lenght arguments

def bio(name,*hobby):
    print(name)
    print(hobby)#o/p takes in tuple

bio('madhu','youtube','coding')


def bio(name,**data):
    print(name)
    print(data)#o/p takes in dict
    for i,j in data.items():#in dict type return use items to fetch data
        print(i,j)
        
    dict = {'me':1,'ma':2}
    for i,j in dict:# this dict no need extra funtions
        print(i,j)

bio('madhu',hobby = 'youtube',job = 'coding')
