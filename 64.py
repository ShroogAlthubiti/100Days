
try:
	print(x)
except NameError:
	print("Variable x is not defined")
except:
	print("something else went wrong")
finally:
	print("the 'try except' is finished")

try:
	print("hello")
except:
	print("something else went wrong")
else:
	print("Nothing went wrong")





