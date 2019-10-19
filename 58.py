import re


txt = "The rain in Spain"
y = re.findall("i", txt)
z=re.search("\s ",txt)
x=re.split("\s",txt)
print(y)
print(z)
print(x)



