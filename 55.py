import json 

x='{"name":"Shroog","age": 22}'
y=json.loads(x)
print(y["age"])

z={
"name":"Shroog",
"age": 22}
s=json.dumps(x)
print(s)

print(json.dumps(43))
print(json.dumps(5.5))
print(json.dumps(True))
print(json.dumps(None))


