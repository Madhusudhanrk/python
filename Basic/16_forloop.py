#INTRO TO for loop **********************************************************************
for i in range(0,10):#range(startNumber,how much numbers fetch,steps asc,desc -1,2 steps ,4 steps)
    if i == 4:
        continue #skips 4 to print and start next sequence
    if i == 7:
        break    # break loop and go out from loop
    # pass THIS KEY WORD WILL SKIP THIS LOOP OR TO SKIP FUNCTION,METHOD
    print(i)
     
else:
    print("Entire loop executed without any break means else part will work")