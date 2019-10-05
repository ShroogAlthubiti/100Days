class Library:
	def __init__(self,book,shelf):
		self.book=book
		self.shelf=shelf
	def print1(self):
		print("Book:",self.book,"\tShelf:",self.shelf)


class science_section(Library):
	def __init__(self,book,shelf,name):
		super().__init__( book,shelf)
		self.name=name
	def print1(self):
		print("Book:",self.book,"\tShelf:",self.shelf,"\tName:",self.name)


L1=Library(300,45)
L1.print1()
S=science_section(300,45,"Physics Books")
S.print1()
S.book=20
S.shelf=4
S.print1()



