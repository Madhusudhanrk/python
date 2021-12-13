print(__name__) #directly this file running means it is __main__
                # if it is running as a module in another file it is file name 27_special_variable

def greetings():
    print("hello madhu from",__name__)

if __name__ == "__main__":
    greetings()