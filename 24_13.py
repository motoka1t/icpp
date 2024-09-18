def getTitanicData(fname):
    data = {}
    data['class'], data['survived'], data['age'] = [], [], []
    data['gender'], data['name'] = [], []
    f = open(fname)
    line = f.readline()
    while line != '':
        split = line.split(',')
        data['class'].append(int(split[0]))
        data['age'].append(float(split[1]))
        if split[2] == 'M':
            data['gender'].append(1)
        else:
            data['gender'].append(0)
        data['survived'].append(int(split[3])) #1が生還
        data['name'].append(split[4:])
        line = f.readline()
    return data

def buildTitanicExamples(filename):
    data = getTitanicData(filename)
    examples = []
    for i in range(len(data['class'])):
        p = Passenger(data['class'][i], data['age'][i], data['gender'][i], data['survived'][i], data['name'][i]])
        examples.append(p)
    return examples
