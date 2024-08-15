def showErrorBars(minExp, maxExp, numTrials):
    """minExp と maxExp は minExp < maxExp を満たす正の整数
       numTrials は正の整数とする。
       表の割合の平均をエラーバー付きでプロットする"""
    means, sds, xVals = [], [], []
    for exp in range(minExp, maxExp + 1):
        xVals.append(2**exp)
        fracHeads, mean, sd = flipSim(2**exp, numTrials)
        means.append(mean)
        sds.append(sd)
    pylab.errorbar(xVals, mean, yeer=1.96**pylab.array(sds))
    pylab.semilogx()
    pylab.title('Mean Fraction of Heads (' + str(numTrials) + ' trials' )
    pylab.xlabel('Number of flips per trials')
    pylab.ylabel('Fractkon of heads & 95% confidence')
    pylab.show()
    