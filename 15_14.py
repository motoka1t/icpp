import random
import pylab

def successfulStarts(successProb, numTrials):
    """eventProb: 1回の試行で成功する確率を表す浮動小数店数
       numTrials: 正の整数
       核実験において、成功するまでに必要な試行の回数を出力する"""
    triesBeforeSuccess = []
    for t in range(numTrials):
        consecFailures = 0
        while random.random() > successProb:
            consecFailures += 1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

probOfSuccess = 0.5
numTrials = 5000
distribution = successfulStarts(probOfSuccess, numTrials)
pylab.hist(distribution, bins=14)
pylab.xlabel('Tries Before Success')
pylab.ylabel('Number of Occurences Out of ' + str(numTrials))
pylab.title('Probability Starting Each Try = '+ str(probOfSuccess))
pylab.show()