
class Person:
	def __init__(self, fname, lname):
		self.firstname=fname
		self.lastname=lname

	def printname(self):
		print(self.firstname,self.lastname)

class Student(Person):
	def __init__(self,fname,lname):
		Person.__init__(self, fname, lname)


P1=Person("Shroog","Abdullah")
P1.printname()
S1=Student("Ali","Ahmad")
S1.printname()
