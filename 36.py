 
def function (n):
 	return lambda a:a*n 


func1=function(2)#n
for x in range(10):
	print(func1(x),end=" ")#a

print("\n")

func2=function(6)#n
#a
print(func1(5))#5*2
print(func2(6))#6*6
print(func1(4))#4*2

