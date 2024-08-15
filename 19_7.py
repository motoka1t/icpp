from scipy import stats
import random
numHyps = 20
sampleSize = 30
population = []
for i in range(5000):
    population.append(random.gauss(0, 1))
sample1s, sample2s = [], []
for i in range(numHyps): #少数標本の組を多く生成
    sample1s.append(random.sample(population, sampleSize))
    sample2s.append(random.sample(population, sampleSize))
#統計学的に異なるかチェックする
numSig = 0
for i in range(numHyps):
    if stats.ttest_ind(sample1s[i], sample2s[i])[1] < 0.05:
        numSig += 1
print('Number of statistically significant (p < 0.05) results =', numSig)