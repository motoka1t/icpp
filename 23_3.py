def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist

def trykmeans(examples, numClusters, numTrials, verbose = False):
    """kmeans関数をnumTrials回呼び出しそして
       最も類似性が小さいクラスタリングを返す"""
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity =  dissimilarity(best)
    trial = 1
    while trial<numTrials:
        try:
            clusters = kmeans(examples, numClusters, verbose)
        except ValueError:
            continue #失敗したらもう一度
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
        trial += 1
    return best
