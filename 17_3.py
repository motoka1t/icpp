
def sampleTimes(times, numExapmples):
    """timesを全走者のフィニッシュタイムを表す浮動小数点数のリストとする
       numExapmlesをintとする
       サイズがnumExapmlesの無作為標本を作り出し
       平均・標準偏差ととともに分布を表すヒストグラムを作り出す"""
    sample = random.sample(times, numExapmples)
    makeHist(sample, 10, 'Sample of Size' + str(numExapmples), 'Minutes to Complete Race', 'Number of Runners')

sampleSize = 40
sampleTimes(times, sampleSize)