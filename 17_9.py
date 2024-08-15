from chapter17 import *

times = getBMIData('bm_results2012.txt')['time']
popMean = sum(times)/len(times)
sampleSize = 200
numBad = 0
for t in range(100000):
    sample = random.sample(times, sampleSize)
    sampleMean = sum(sample)/len(sample)
    se = stdDev(sample)/sampleSize**0.5
    if abs(popMean - sampleMean) > 1.96*se:
        numBad += 1
print('Fraction outside 95% confidence interval = ', numBad/100000)