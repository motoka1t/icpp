import pylab 

principal = 10000 #初期投資額
interestRate = 0.05
years = 20
values = []
for i in range(years + 1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values)
pylab.title('5% Growth, compounted Annually')
pylab.xlabel('Yeas of Compounding')
pylab.ylabel('Balus of Principal ($)')
pylab.show()
