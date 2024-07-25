def walk(f, d, numSteps):
    """f: Fieldクラスのオブジェクト
    d: Drunkクラスのオブジェクト
    numSteps: ０以上の整数
    dをnumSteps回移動し、酔歩の初期位置と最終位置との差を出力する"""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """numSteps: 0以上の整数
    numTrials: 正の整数
    dClass: Drunkのサブクラス
    numSteps回移動する酔歩を、numTrials回シミュレートする
    各実験の初期位置と最終位置の差をリストにして出力する"""
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """walkLengths: 0以上の整数のシークエンス
    numTrials: 正の整数
    dClass: Drunkのサブクラス
    walkLengthsの各要素を酔歩の移動回数として、numTrials回の酔歩を
    シミュレートするsimWalksを実行し、結果を出力する"""
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), ' Min =', min(distances))
