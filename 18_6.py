def getHorizontalSpeed(quadFit, minX, maxX):
    """quadFitには2次多項式の要素が入っているとする
       minXとmaxXをインチ単位の距離と仮定する
       水平方向の速度を返す(単位はフィート/秒)"""
    inchesPerFoot = 12
    xMid =(maxX-minX)/2
    a, b, c = quadFit[0], quadFit[1], quadFit[2]
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*inchesPerFoot
    t = (2*yPeak/g)**0.5 # 最高点から標的までの所要時間(秒)
    print('Horizontal speed =', int(xMid/(t*inchesPerFoot)), 'feet/sec.')

    