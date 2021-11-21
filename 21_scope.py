
a = 10

def value():
    print(a)# o/p 10 can use global value

value()

def value():
    a = 15 #local variable
    print(a)# o/p 15

value()

def value1():
    global a #fetching reference of global variable
    a = a  + 5 
    print("inside",a)
value1()
print("outside",a)

# globals()['variable name'] = assingment #value will be changed