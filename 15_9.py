def flipPlot2(minExp, maxExp, numTrials):
    """minExpとmaxExpはみnExp<maxExpを満たす正の整数
    numTrialsは正の整数とする
    2**minExpから2**maxExp回のコイン投げをぬmTrials回
    行った結果の要約をプロットする"""
    ratiosMeans, diffsMeans, ratiosSDs, diffsSDs = [], [], [], []
    ratiosCVs, diffsCVs, xAxis = [], [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios, diffs = [], []
        for t in range(numTrials):
            numHeads, numTails = runTrial(numFlips)
            ratios.append(numHeads/float(numTrials))
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratiosCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString = '(' + str(numTrials) + " Trials)" 
    title = 'Mean Head/Tails ratios' + numTrialsString
    makePlot(xAxis, ratiosMeans, title, 'Number of flips', 'Mean Heads/Tails', 'ko', logX = True)
    title = 'SD Hrads/Tails Ratios' + numTrialsString
    makePlot(xAxis, ratiosSDs, title, 'Number of flips', 'Standard Deviation', 'ko', logX = True, logY = True)
    title = 'Mean abs(#Heads - #Tails)' + numTrialsString
    makePlot(xAxis, diffsMeans, title, 'Number of flips', 'Mean abs(#Heads-#Tails)', 'ko', logX = True, logY = True)
    title = 'SD abs(#Heads-#Tails)' + numTrialsString
    makePlot(xAxis, diffsSDs, title, 'Number of flips', 'Standard Deviation', 'ko', logX = True, logY = True)
    title = 'Coeff. of Var. abs(#Heads-#Tails)' + numTrialsString
    makePlot(xAxis, diffsCVs, title, 'Number of flips', 'Coeff. of Var.', 'ko', logX = True)
    title = 'Coeff. of Vars. Heads/Tails Ratio' + numTrialsString
    makePlot(xAxis, ratiosCVs, title, 'Number of flips', 'Coeff. of Var.', 'ko', logX=True, logY=True)

