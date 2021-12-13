# class Computer:
#     def __init__(self,brand,price):
#         self.brand = brand # once the value assigned with class object it will be avail for entire class
#         self.price = price
    
#     def my_lap(self,name):
#         self.name = name # once the value assigned with class object it will be avail for entire class
#         print(name, "like",self.brand,"laptops")

#     def my_lap1(self):
#         print(self.name,"laptops")# once the value assigned with class object it will be avail for entire class

# person1 = Computer('Dell',50000)

# person1.my_lap("madhu")

# person1.my_lap1()# once the value assigned with class object it will be avail for entire class

# person2 = Computer('Apple',150000)

# person2.my_lap('Ravi')

class my_age:
    def __init__(self,age):
        self.age = age
    def compare(self,manoj_age_obj):
        if self.age == manoj_age_obj.age:
            return True
        else:
            return False

madhu_age = my_age(23)
manoj_age = my_age(23)

if madhu_age.compare(manoj_age): #compare(madhu_age,manoj_age)
    print("same age") 
else:
    print("not same age")

#constructor will create memory and its size for the class  based on variables


#namespace is a place were we can create/save variables/object

"""
Two types of variables:
1.Class variables
        eg: class name:
                var = 10 it belongs to every obj in class and it is outside every method
2.Instance variable
          It is inside methods and works based on obj calling but if we change value in 1 method won't affect in other method value.
"""