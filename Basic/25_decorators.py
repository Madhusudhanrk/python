#INTRO TO decorators *********************************************************************

# def div(a,b): 
#     print(a/b)

# # div(2,4)# numerator is smaller than denaminator

# def smart_div(func): 
#     # div(a=2,b=4) or func(a=2,b=4)
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)#div(a value,b value)
#     return inner #exit from innerfunc

# div = smart_div(div)

# div(2,4)

#change the behaviour of the existing function

#decorators add aditional functionality without modifying existing function

def check(func):
    def inner(a,b):
        if b==0:
            print("can't divide by 0")
            return 
        func(a,b)
    return inner

@check # div = check(div) equals to this code
def div(a,b): 
    return a/b

print(div(10,0))

 