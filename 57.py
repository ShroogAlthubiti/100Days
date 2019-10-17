import re


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("i", txt)
print(y)

if (x):
	print("YES We have a match!")
else:
	print("No match")