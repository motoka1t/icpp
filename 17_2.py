import pylab
from stddev import stdDev

def getBMIData(filename):
    """与えられたファイルの内容を読み込む
       0.氏名(string)、1.性別(string)、2.年齢(int)
       3.区分(走/車椅子)(int)、4.出身国(atring)
       5.総合タイム(float)"""
    data = {}
    f = open(filename)
    line = f.readline()
    data['name'], data['gender'], data['age'] = [], [], []
    data['division'], data['country'], data['time'] = [], [], []
    while line != '':
        split = line.split(',')
        data['name'].append(split[0])
        data['gender'].append(split[1])
        data['age'].append(int(split[2]))
        data['division'].append(int(split[3]))
        data['country'].append(split[4])
        data['time'].append(float(split[5][:-1])) #\nを取り除く
        line = f.readline()
    f.close()
    return data

def makeHist(data, bins, title, xLabel, yLabel):
    pylab.hist(data, bins)
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    mean = sum(data)/len(data)
    std = stdDev(data)
    pylab.annotate('Mean = ' + str(round(mean, 2)) + '\nSD = ' + str(round(std, 2)), fontsize = 20, xy = (0.65,0.75), xycoords='axes fraction')
    pylab.show()

times = getBMIData('bm_results2012.txt')['time']
makeHist(times, 20, '2012 Boston Marathon', 'Minutes to Complete Race', 'Number of Runners')