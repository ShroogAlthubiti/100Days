def my_function (name):
	for x in name:
		print(x)
name=["Shroog", "Ali", "Ahmad"]
my_function(name)

def multiply (num):
	return 5*num
print(muliply(5))
print(muliply(6))

def child(child1,child2,child3):
	print("the youngest child is",child3)
child(child1="Emil",child2="jonh",child3="aliee")

def child1(*Kids):
	print("the youngest child is",Kids[2])
child1("Emil","aliee","jonh")

def recursion(K):
	if(K>0):
		result=K+recursion(K-1)
		print(result)
	else:
		result=0
	return result
print("Recursion Example Result")
recursion(4)