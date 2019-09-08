
set1={}
set2={2,3,4,5,"Shroog","Shroog",2}
print(set1)

for x in set2:
	print(x)

print("Shroog" in set2)
set2.add(1)
set2.update([6,7])
print(set2)