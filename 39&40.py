
#Q1: 
def recursion(N,P):
	
	if(P==0):
		return 1
	else:
		return N*recursion(N,P-1)
	
print(recursion(5,3))
print(recursion(4,2))

#Q2:
num=[-4,-6,-5,-1,2,3,7,9,88]
result = list(filter(lambda x: (x >0),num))  
  # printing the result 
print(result) 
		


