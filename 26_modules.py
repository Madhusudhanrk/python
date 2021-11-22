# modules means keep different bunch of codes in multiple files
# and calling modules to the file were we need the code
# example math module imported while we work on math like creating own model CALC

# from calc import *

# print(add(2,3))
# print(sub(2,3))
# print(mul(2,3))

import calc
print(calc.add(2,3))

#packages contain separate folder and we can import packages like
# from foldername import a file or b file
# a.method name