def readMammalData(fName):
    dataFile = open(fName, 'r')
    numFeatures = 0
    #ファイルの先頭の処理
    for line in dataFile: #特頭数を調べる
        if line[0:6] =='#Label' #特徴の終了を示す
            break
        if line[0:5] != '#Name'
            numFeatures += 1

    #featureVals、speciesNamesとlabelListの生成
    featureVals, speciesNames, labelList = [], [], []
    for i in range(numFeatures):
        featureVals.append([])

    #コメント後の、行ごとの処理
    for line in dataFile:
        #改行の除去、その後分割
        dataLine = line[:-1].split(',')
        speciesNames.append(dataLine[0])
        classLabel = dataLine[-1]
        labelList.append(classLabel)
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))

    #特徴ベクトルを含むリストを作るためにfeatureValsを使う
    #それぞれの哺乳類について
    featureVectorList = []
    for mamal in range(len(speciesNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][mamal])
        featureVectorList.append(featureVector)
    return featureVectorList, labelList, speciesNames

def buildMamalExamples(featureList, labelList, speciesNames):
    examples = []
    for i in range(len(speciesNames)):
        features = pylab.array(featureList[i])
        example = Example(speciesNames[i], features, labelList[i])
        examples.append(example)
    return examples