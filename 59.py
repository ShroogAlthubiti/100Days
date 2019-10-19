import re


txt = "The rain in Spain"
x = re.sub("\s","9", txt)
print(x)

x = re.sub("\s","9", txt, 2)
print(x)

x = re.search(r"\bS\w+", txt)
print(x.span())
print(x.string)
print(x.group())
