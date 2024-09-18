#男性、女性別にトレーニングデータセットを作る
ageM, ageW, timeM, timeW = [], [], [], []
for e in training:
    if e.getLabel() == 'M':
        ageM.append(e.getAge())
        timeM.append(e.getTime())
    else:
        ageW.append(e.getAge())
        timeW.append(e.getTime())
#プロットを見やすくするためにダウンサンプルをする
ages, times = [], []
for i in random.sample(range(len(ageM)), 300):
    ages.append(ageM[i])
    times.append(timeM[i])
#標本の散布図を作成する
pylab.plot(ages, times, 'yo', markersize=6, label='Men')
ages, times = [], []
for i in random.sample(range(len(ageW)), 300):
    ages.append(ageW[i])
    times.append(timeW[i])
pylab.plot(ages, times, 'k', markersize=6, label='Women')
#2つの、1次線形回帰モデルを学習する
mModel = pylab.polyfit(ageM, timeM, 1)
fModel = pylab.polyfit(ageW, timeW, 1)
#モデルに対応した直線をプロットする
xmin, xmax = 15, 85
pylab.plot((xmin, xmax), (pylab.polyval(mModel,(xmin, xmax))), 'k', label='Men')
pylab.plot((xmin, xmax), (pylab.polyval(fModel,(xmin, xmax))), 'k--', label='Women')
pylab.title('Linear Regression Models')
pylab.xlabel('Age')
pylab.ylabel('Finishing Time (minutes)')
pylab.legend()