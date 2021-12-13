
a = 5
for i in range(a):
    for j in range(i+1):
        print("* ",end="")
    print()


for i in range(a):
    for j in range(a-i):
        print("* ",end="")
    print()

for i in range(a):
    for j in range(a-i):
        print(" ",end="")
    for k in range(i+1):
        print("* ",end="")
    print()