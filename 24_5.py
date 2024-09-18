import pylab

def findK(training, minK, maxK, numFolds, label):
    #ある値の範囲の奇数kに対する平均正確度を計算する
    accuracies = []
    for k in range(minK, maxK+1, 2):
        score = 0.0
        for i in range(numFolds):
            #計算時間を計算するためのダウンサンプル
            fold = random.sample(training, min(5000, len(training)))
            examples, testSet = divide80_20(fold)
            truePos, falsePos, trueNeg, falseNeg = KNearestClassify(examples, testSet, label, k)
            score += accuracy(truePos, falsePos, trueNeg, falseNeg)
        accuracies.append(score/numFolds)
    pylab.plot(range(minK, maxK+1, 2), accuracies)
    pylab.title('Average Accuracy vs k' + str(numFolds) + ' folds)')
    pylab.xlabel('k')
    pylab.ylabel('accuracy')

findK(training, 1, 21, 1, 'M')