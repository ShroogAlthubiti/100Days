#class 
class Student:
	name="Shroog"

	def __init__(self,name,id):
		self.name=name
		self.id=id
	def func (self):
		print("Student Name:  " , self.name ,"\nStudent ID: ", self.id )


#create object
S1=Student("Shroog",11234)
S1.func()

S2=Student("Ali",12234)
print("ID: ",S2.id)