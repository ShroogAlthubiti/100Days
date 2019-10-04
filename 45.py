mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
class num :
	def __iter__(self):
		self.a=1
		return self

	def __next__(self):
		if self.a<=20:
			x=self.a
			self.a+=1
			return x
		else:
			raise StopIteration
myclass=num()
myit2=iter(myclass)

for x in myit2:
	print(x)

	
