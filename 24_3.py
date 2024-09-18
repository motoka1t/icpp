def findKNearest(example, exampleSet, k):
    kNearest, distances = [], []
    #最初のk個の標本からなるリストと、それらとexampleの距離のリストを作る
    for i in range(k):
        kNearest.append(exampleSet[i])
        distances.append(example.featureDist(exampleSet[i]))
    maxDist = max(distances) #Get maximum distance
    #まだ考えられていないexampleSetの標本に対して
    for e in exampleSet[k:]:
        dist = example.featureDist(e)
        if dist < maxDist:
            #最も遠い距離にある標本を、標本eで置き換える
            maxIndex = distances.index(maxDist)
            kNearest[maxIndex] = e
            distances[maxIndex] = dist
            maxDist = max(distances)
    return kNearest, distances

def KNearestClassify(training, testSet, label, k):
    """trainingとtestSetは標本のリスト、kは整数であるとする
    testSetの標本が、与えられたlabelを持つ標本なのかどうかを
    k-近傍分類器を使って予想する。真陽性(true positive)、
    偽陽性(false positive)、真陰性(true negative)、
    偽陰性(false negative)の標本の数を返す"""
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet:
        nearest, distances = findKNearest(e, training, k)
        #投票を行う（多数決なので）
        numMatch = 0
        for i in range(len(nearest)):
            if nearest[i].getLabel()==label:
                numMatch += 1
        if numMatch > k//2: #判断はラベルと同じ
            if e.getLabel()==label:
                truePos += 1
            else:
                falsePos += 1
        else: #判断はラベルと異なる
            if e.getLabel()!=label:
                trueNeg += 1
            else:
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg