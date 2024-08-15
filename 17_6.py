import random
import pylab
from stddev import variance

def plotMeans(numDicePerTrial, numDiceThrown, numBins, legend, color, style):
    means = []
    numTrials = numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals = 0
        for j in range(numDicePerTrial):
            vals += 5*random.random()
        means.append(vals/numDicePerTrial)
    pylab.hist(means, numBins, color = color, label = legend, weights = pylab.array(len(means)*[1])/len(means), hatch = style)
    return sum(means)/len(means), variance(means)

mean, var = plotMeans(1, 100000, 11, '1 die', 'w', '*')
print('Mean of rolling 1 die =', round(mean, 4), 'Variance =', round(var, 4))
mean, var = plotMeans(100, 100000, 11, 'Mean of 100 die', 'w', '//')
print('Mean of rolling 100 die =', round(mean, 4), 'Variance =', round(var, 4))
pylab.title('Rolling Continuous Die')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()