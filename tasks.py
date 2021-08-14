#ODD OR EVEN task1
#  num = int(input("Enter a number:\n"))
# if(num%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")

#ODD OR EVEN limit

# limit = int(input("Enter a Limit number:\n"))
# limit = limit+1
# for i in range(1,limit):
#     if(i%2!=0):
#         print(i)

#STRING REVERSE task2

#Method 1
# def reverse_string(str):             
#     strrev = ""
#     for i in str:
#         strrev = i + strrev
#     return strrev

# print(reverse_string(input("Enter any thing:\n")))

#Method 2

# def reverse_string(str): 
#     strrev = str[::-1]   
#     return strrev         
# print(reverse_string(input("Enter any thing:\n")))

#SWAPPING task3
# a=3
# b=4
# t=""
# print("Before Swap:",a,b)
# t = a
# a = b
# b = t
# print("After Swap:",a,b)

#Bubble sort task4
# num = [5,3,8,6,7,2]
# num = [2,7,1,4]
# length = len(num)
# # print(length)
# for i in range(length-1,0,-1):# length of iterations
#     print(i)
#     for j in range(i):# every iterations were moved bigger value to last so reduce length 1 
#         if(num[j]>num[j+1]):
#             temp = num[j]
#             num[j] = num[j+1]
#             num[j+1] = temp
# print(num)



# def sort(num_list):
#     length = len(num_list)
#     for i in range(length-1,0,-1):
#         for j in range(i):
#             if(num_list[j]>num_list[j+1]):
#                 temp = num_list[j]
#                 num_list[j] = num_list[j+1] 
#                 num_list[j+1] = temp
#     return num_list
# print(sort([2,1,5,3,2]))