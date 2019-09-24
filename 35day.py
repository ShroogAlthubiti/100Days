

x = lambda a: a+10
print(x(5))

x = lambda a, b: a*b
print(x(5,7))

x = lambda a, b , c: a+b+c
print(x(5,4,2))

Discount=lambda ratio ,amount: amount-((ratio/100)*amount)
print(Discount(15,100))
print(Discount(20,300))