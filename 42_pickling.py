import pickle

f = open("test.txt","wb")
dic = {"name":"madhu","age":20}
pickle.dump(dic,f)
f.close()

f = open("test.txt","rb")
print(pickle.load(f))
f.close()