dictionary={"name":"shroog " , "age": 22 ,"year":1997 }
print(dictionary)
# change value
x=dictionary["name"]
print(x)
# change value use get
x=dictionary.get("age")
print(x)

dictionary["age"]=23
print(dictionary.items())
   #print 
for x in dictionary.values():
	print(x)
  
for x in dictionary.items():
	print(x)


