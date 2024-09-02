def contrivedTest2(numTrials, k, verbose = False):
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 8
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    d2Samples = genDistribution(xMean+3, xSD, yMean, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    d3Samples = genDistribution(xMean, xSD, yMean+3, ySD, n, 'C')
    plotSamples(d2Samples, 'kx')

    clusters = trykmeans(d1Samples+d2Samples+d3Samples, k, numTrials, verbose)
    pylab.ylim(0.11)
    print('Final Result has dissimilarity', round(dissimilarity(clusters), 3))
    for c in clusters:
        print(" ", c)