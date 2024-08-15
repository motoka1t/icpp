from chapter17 import *

times = getBMIData('bm_results2012.txt')['time']
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(50, 2000, 200)
for sampleSize in sampleSizes:
    sampleMeans = []
    for t in range(20):
        sample = random.sample(times, sampleSize)
        sampleMeans.append(sum(sample)/sampleSize)
    meanOfMeans.append(sum(sampleMeans)/len(sampleMeans))
    stdOfMeans.append(stdDev(sampleMeans))
pylab.errorbar(sampleSizes, meanOfMeans, yerr = 1.96*pylab.array(stdOfMeans), label='Estimated mean and 95% confidence interval')
pylab.xlim(0, max(sampleSizes) + 50)
pylab.axhline(sum(times)/len(times), linestyle='--', label='Population mean')
pylab.title('Estimate of Mean Finishing Time')
pylab.xlabel('Sample Size')
pylab.ylabel('Finishing Time (minutes)')
pylab.legend(loc = 'best')
pylab.show()