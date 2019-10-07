x=200 #global
y=500
def func():
	x=300 #local
	global y 
	y=100
	print(x)

func()
print(x)
print(y)