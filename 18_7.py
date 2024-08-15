import pylab

vals = []
for i in range(10):
    vals.append(3**i)
pylab.plot(vals, 'ko', label = 'Actual points')
xVals = pylab.arange(10)
fit = pylab.polyfit(xVals, vals, 5)
yVals = pylab.polyval(fit, xVals)
pylab.plot(yVals, 'kx', label = 'Predicted points', markeredgewidth=2, markersize=10)
pylab.title('Fiting y = 3**x')
pylab.legend(loc='best')
pylab.show()