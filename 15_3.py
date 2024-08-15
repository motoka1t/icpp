def regressToMean(numFlips, numTrials):
    #numFlips回の試行で表が出る割合
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    #極端な値が出る試行とその次の試行をえる
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    #結果をプロットする。
    pylab.plot(range(len(extremes)), extremes, 'ko', label = 'Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1, len(extremes)+1)
    pylab.xlabel('Extreme Example and NextTrial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression in the Mean')
    pylab.legend(loc = 'best')
    