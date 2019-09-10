dictionary={"name":"shroog " , "age": 22 ,"year":1997 }

if "age" in dictionary:
	print("yes")

print(len(dictionary))

dictionary["study"]="computer science"
print(dictionary)

dictionary.pop("year")
print(dictionary)

dictionary.popitem()
print(dictionary)

dictionary.clear()
print(dictionary)

del dictionary
print(dictionary)

