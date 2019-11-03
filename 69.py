import os
f = open("file.txt", "rt") # r = read , t= text 
print(f.read())

f = open("file.txt", "r")

print("-------Read first 5 letters------ \n",f.read(5))
print("-------Read first line ------ \n",f.readline())
print(f.readline())
print("----- Read by use for statement------")
f = open("file.txt", "r")
for x in f:
	print(x)
f.close()
f=open("file2.txt","a")
f.write("Now the file has more content!")
f.close()
f=open("file2.txt","r")
print(f.read())

f=open("file3.txt","x")
if os.path.exists("file2.txt"):
	os.remove("file2.txt")
else:
	print("the file does not exist")