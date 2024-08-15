def getData(filename):
    dataFile = open(filename, 'r')
    distances = []
    masses = []
    dataFile.readline() #ヘッダは無視する
    for line in dataFile:
        d, m = line.split(' ')
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return(masses, distances)
