def readMammalData(fName, scale):
    #コード23.9のものと同じ
    dataFile = open(fName, 'r')
    numFeatures = 0
    #ファイルの先頭の処理
    for line in dataFile: #特頭数を調べる
        if line[0:6] =='#Label' #特徴の終了を示す
            break
        if line[0:5] != '#Name'
            numFeatures += 1

    #featureVals、speciesNames、labelListを作る
    #コード23.9のものと同じ
    featureVals, speciesNames, labelList = [], [], []
    for i in range(numFeatures):
        featureVals.append([])

    #ファイルのコメント以下の部分に対して処理を続ける
    #コード23.9のものと同じ
    for line in dataFile:
        #改行の除去、その後分割
        dataLine = line[:-1].split(',')
        speciesNames.append(dataLine[0])
        classLabel = dataLine[-1]
        labelList.append(classLabel)
        for i in range(numFeatures):
            featureVals[i].append(float(dataLine[i+1]))

    #特徴ベクトルを含むリストを作るためにfeatureValsを使う
    #それぞれの哺乳類について、指示の通り特徴ベクトルをスケーリング
    for i in range(numFeatures):
        featureVals[i] = scale(featureVals[i])
    featureVectorList = []
    for mamal in range(len(speciesNames)):
        featureVector = []
        for feature in range(numFeatures):
            featureVector.append(featureVals[feature][mamal])
        featureVectorList.append(featureVector)
    return featureVectorList, labelList, speciesNames

def testTeeth(numClusters, numTrials, scale = lambda x: x):
    features, labels, species = readMammalData('dentalFormulas.txt', scale)
    examples = buildMammalExamples(features, labels, species)

    ###testTeethの残りの部分はコード23.10のものと同じ###
    bestClustering = trykmeans(examples, numClusters, numTrials)
    for c in bestClustering:
        names = ''
        for p in c.members():
            names += p.getName() + ', '
        print('\n' + names[:-2])#続くコンマとスペースを取り除く
        herbivores, carnivores, omnivores = 0, 0, 0
        for p in c.members():
            if p.getLabel() =='0':
                herbivores += 1
            elif p.getLabel() == '1':
                carnivores += 1
            else:
                omnivores += 1
        print(herbivores, 'herbivores,', carnivores, 'carnivores,', omnivores, 'omnivores')
        