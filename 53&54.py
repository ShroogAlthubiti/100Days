
import module
import datetime

print("1+8 =",module.add(1,8))
print("4-2 =",module.minus(4,2))
print("6*6 =",module.multiply(6,6))
print("8/2 =",module.divide(8,2))

date=datetime.datetime.now()
print(date.strftime("%c"))

t=datetime.date.today()
print(t)
x=int(t.strftime("%d"))
print(x-1)
print(x+1)



