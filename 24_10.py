def applyModel(model, testSet, label, prob = 0.5):
    #すべてのテストデータに対する特徴ベクトルからなるベクトルを作る
    testFeatureVecs = [e.getFeatures() for e in testSet]
    probs = model.predict.proba(testFeatureVecs)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if testSet[i].getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else:
            if testSet[i].getLabel() != label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg

examples = buildMarathonExamples('bm_result2012.txt')
training, test = divide80_20(examples)

featureVecs, labels = [], []
for e in training:
    featureVecs.append([e.getAge(), e.getTime()])
    labels.append(e.getLabel())
model = sklearn.linear_model.LogisticRegression().fit(featureVecs, labels)
print('Feature weights for label M:', 'age =', str(round(model.coef_[0][0], 3)) + ',', 'time =', round(model.coef_[0][1], 3))
truePos, falsePos, trueNeg, falseNeg = applyModel(model, test, 'M', 0.5)
getStats(truePos, falsePos, trueNeg, falseNeg)