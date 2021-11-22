f = open('file.txt')
print(f.read())

f = open('file.txt',"r")
print(f.read(5))
print(f.readline())
f.close()

f = open('file.txt',"a")
f.write("hi mom")
f.close()

f = open('file.txt',"r")

print(f.read())


f = open('file.txt',"w") #rewrite everything
f.write("hi mom")
f.close()

f = open('file.txt',"r")

print(f.read())
f.close()

import os
if os.path.exists('file.txt'):
    os.remove('file.txt')
else:
    print("The file does not exist")