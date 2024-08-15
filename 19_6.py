from chapter17 import *
from scipy import stats

data = getBMIData('bm_results2012.txt')
countriesToCompare = ['BEL', 'BRA', 'FRA', 'JPN', 'ITA']
#国別の女性フィニッシュタイムの辞書を作成する
countryTimes = {}
for i in range(len(data['name'])): #各ランナーに対して
    if data['country'][i] in countriesToCompare and data['gender'][i] == 'F':
        try:
            countryTimes[data['country'][i]].append(data['time'][i])
        except KeyError:
            countryTimes[data['country'][i]] = [data['time'][i]]

#各国のフィニッシュタイムを計算する
for c1 in countriesToCompare:
    for c2 in countriesToCompare:
        if c1 < c2: #各ぺあを丁度１回比較するために!=出なく<を使う
            pVal = stats.ttest_ind(countryTimes[c1], countryTimes[c2], equal_var = False)[1]
            if pVal < 0.05:
                print(c1, 'and', c2, 'have significantly different means.', 'p-value =', round(pVal, 4))