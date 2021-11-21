#Finding factorial of a number

# def fact(n):
#    f = 1
#    for i in range(1,n+1):
#        f = f * i
#    return f
# n=4
# print(fact(n))#o/p 24

#Using Recursion finding factorial of a number

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

n=4
print(fact(n))#o/p 24
