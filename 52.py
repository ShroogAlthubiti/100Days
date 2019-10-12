import datetime 

x= datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

y= datetime.datetime(1997,3,3)
print(y)
print(y.strftime("%B"))


z=datetime.date(2000,2,5)
print(z.strftime())

print(dir(datetime))


