import pylab
def compareAnimals(animals, precision):
    """animalsはAnimalオブジェクトのリスト、precisionは非負の整数とする
       それぞれのAnimal間のユークリッド距離の表を作る"""
    #行と列のラベルを得る
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowlabels = columnLabels[:]
    tableVals = []
    #Animal間の距離を得る
    #それぞれの行について
    for a1 in animals:
        row = []
        #それぞれの列について
        for a2 in animals:
            if a1==a2:
                row.append('--')
            else:
                distance = a1.distance(a2)
                row.append(str(round(distance, precision)))
        tableVals.append(row)
    #表を作る
    table = pylab.table(rowLabels = rowlabels, colLabels=columnLabels, cellText=tableVals, cellLoc='center', loc='center', colWidths=[0.2]*len(animals))
    table.scale(1, 2.5)
    pylab.savefig('sistance')