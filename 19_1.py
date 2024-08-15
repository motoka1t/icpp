import numpy
import pylab

tStat = -2.13165598142 #PED-Xの例のt検定量
tDist = []
numBins = 1000
for i in range(10000000):
    tDist.append(numpy.random.standard_t(198))

pylab.hist(tDist, bins = numBins, weights=pylab.array(len(tDist)*[1.0])/len(tDist))
pylab.axvline(tStat, color='w')
pylab.axvline(-tStat, color='w')
pylab.title('T-distribution with 198 Degrees of Freedom')
pylab.xlabel('T-statics')
pylab.ylabel('Probability')
pylab.show()
