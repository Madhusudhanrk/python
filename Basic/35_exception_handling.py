a=5
b=0

try:
    print("start")
    print(a/b)
except Exception as e:
    if b==0:
        print("we can't divide by 0")
    else:
        print(e)
finally:
    print("stop")