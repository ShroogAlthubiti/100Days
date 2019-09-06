# Q1:
list1=[2,6,4,8,3,1,5,7]
print("Befor sort:",list1)
list1.sort()
print("After sort:", end = "[")
for x in list1:
	print(x , end = ", ")
print("]")	
list1.reverse()
print("reverse:",list1)
list1.insert(1,8)
print("count 8:",list1.count(8))

#Q2:
tuple1=("java", "python", "swift")

if "python" in tuple1:
	print("Yes , python in tuple1")

