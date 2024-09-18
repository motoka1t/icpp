def testModels(examples, numTrials, printStats, printWeights):
    stats, weights = [],[[], [], [], [],[]]
    for i in range(numTrials):
        training, testSet = divide80_20(examples)
        xVals, yVals = [], []
        for e in training:
            xVals.append(e.getFeatures())
            yVals.append(e.getLabel())
        xVals = pylab.array(xVals)
        yVals = pylab.array(yVals)
        model = sklearn.linear.model.LogisticRegression().fit(xVals, yVals)
        for i in range(len(Passenger.features)):
            weights[i].append(model.coef_[0][i])
        truePos, falsePos, trueNeg, falseNeg = applyModel(model, testSet, 1, 0.5)
        auroc = buildROC(model, testSet, 1, None, False)
        tmp = getStats(truePos, falsePos, trueNeg, falseNeg, False)
        stats.append(tmp + (auroc,))
    print('Average for', numTrials, ' trials')
    if printWeights:
        for feature in range(len(weights)):
            featureMean = sum(weights[feature])/numTrials
            featureStd = stdDev(weights[feature])
            print('Mean of weight', Passenger.features[feature], '=', str(round(featureMean, 3)) + ',', '95% confidence interval =', round(1.96*featureStd, 3))
    if printStats:
        summarizeStats(stats)
        