def prevalenceClassify(training, testSet, label):
    """trainingとtestSetは標本のリストであるとする
    testSetのそれぞれの標本のラベルは、クラスレベルと同じかどうか
    prevalence-based分類器を使って予想する。
    真陽性(true positive)、偽陽性(false positive)、
    真陰性(true negative)、偽陰性(false negative)の数を返す"""
    numWithLabel = 0
    for e in training:
        if e.getLabel()==label:
            numWithLabel += 1
    probLabel = numWithLabel/len(training)
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        if random.random() < probLabel: #eがlabelクラスであると判断
            if e.getLabel() == label:
                truePos += 1
            else:
                falsePos += 1
        else: #eがlabelクラスでないと判断
            if e.getLabel()!=label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg    