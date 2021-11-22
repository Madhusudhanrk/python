#iterator takes sequence datatypes

#iterator uses two functions 
#1.iter() it will convert sequence to iterator
#2.next() it will print next next values

names = ['madhu','manoj','ravi']
obj  = iter(names)
print(next(obj))
print(next(obj))
print(next(obj))

#we can use loop to iterate iterable obj
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


# class MyNumbers:
#     def __iter__(self):
#        self.a = 1
#        return self 

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# class numbers():
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# num = numbers()
# it = iter(num)
# print(next(it))
# print(next(it))
# print(next(it))

class numbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
        if self.a<=20:
          x = self.a
          self.a += 1
          return x
        else:
              raise StopIteration
num = numbers()
myiter = iter(num)
for i in myiter:
  print(i)