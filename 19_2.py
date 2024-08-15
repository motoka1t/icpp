import scipy

controlTimes = [] 
treatmentTimes = [] 

controlMean = sum(controlTimes)/len(controlTimes)
treatmentMean = sum(treatmentTimes)/len(treatmentTimes)
print('Treatment mean - control mean =', treatmentMean - controlMean, 'minutus')
twoSampleTest = scipy.stats.ttest_ind(treatmentTimes, controlTimes, equal_var = False)
print('The t-statistic from two-sample test is', twoSampleTest[0])
print('The p-value from two sample test is', twoSampleTest[1])
