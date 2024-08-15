import pylab
def plotHousing(impression):
    """impressionは、flat、volatile、fair
       のいずれかの値を取る文字列と仮定する
       時間経過に伴う住宅価格の棒グラフを生成する"""
    f = open('midWestHousingPrices.txt', 'r')
    #ファイルの各行は、アメリカ合衆国中西部の四半期ごとの価格を表す
    labels, prices = ([], [])
    for line in f:
        year, quater, price = line.split()
        label = year[2:4] + '\n Q' + quater[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters =pylab.arange(len(labels)) #棒グラフのx座標
    width = 0.3 #棒グラフの幅
    pylab.bar(quarters, prices, width)
    pylab.xticks(quarters+width/2, labels)
    pylab.title('Housing Prices in U.S. Midwest')
    pylab.xlabel('Quarter')
    pylab.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        pylab.ylim(10, 500)
    elif impression == 'volatile':
        pylab.ylim(100, 200)
    elif impression == 'fair':
        pylab.ylim(150, 250)
    else:
        raise ValueError
    
plotHousing('fair')
pylab.figure()
plotHousing('volatile')
