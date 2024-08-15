def cropsSim(handsPerGame, numGames):
    """handsPerGamesとnumGamesは1以上の整数(int)と仮定する
       handsPerGameの手から成るゲームをnumGames回プレイし
       その結果を表示する"""
    games=[]

    #ゲームをnumGame回プレイする
    for t in range(numGames):
        c = CrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)
    
    #各ゲームの統計値を求める
    pROIPerGame, dpROIPerGame = [], []
    for g in games:
        wins, losses = g.passResults()
        pROIPerGame.append((wins-losses)/float(handsPerGame))
        wins, losses, pushes = g.dpResults()
        dpROIPerGame.append((wins-losses)/float(handsPerGame))
    
    #統計値の概要を求めて表示する
    meanROI = str(round(100*sum(pROIPerGame)/numGames, 4))+ '%'
    sigma = str(round(100*stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev =', sigma)
    meanROI = str(round(100*sum(dpROIPerGame)/numGames, 4))+ '%'
    sigma = str(round(100*stdDev(dpROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev =', sigma)    
     