#split
string  = "hello madhusudhan"

print(string.split(' '))

#join
string = ['hello','madhusudhan']

print(' '.join(string))

#capitalize each letter of the starting word
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#count
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

#format 
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#isdigit Returns True if the string is an identifier
txt = "50800"

x = txt.isdigit()

print(x)

# Replace the word "bananas":

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

# Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")