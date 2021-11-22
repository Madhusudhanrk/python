def sq():
    i = 1
    while i<=10:
        yield i*i
        i += 1

val = sq()
for i in val:
    print(i)

#generator used for generating iterator without we creating iterator
# for that it uses yield keyword it return the value in iter format and it won't break execution like return
# genarator create iter obj using next or for loop we can collect data
# if we need to fetch values from database we need one iterable and loop to work with all data were no need to take all values at a time and wasting memory