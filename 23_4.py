import random
import pylab

def kmeans(examples, k, verbose = False):
    #初期のk値のランダムな重心を選び
    #sそれぞれに重心に対してクラスタを生成する
    initialCentroids = random.sample(examples, k)
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))
    
    #重心が変化しなくなるまで繰り返す
    converged = False
    numIterations = 0
    while not converged:
        numIterations += 1
        #k個の空のリストからなるリストを作る
        newClusters = []
        for i in range(k):
            newClusters.append([])
        #標本それぞれeについて
        for e in examples:
            #eに最も近い重心を見つける
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1,k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #適切なクラスターの標本リストにeを加える
            newClusters[index].append(e)

        for c in newClusters:#空のクラスタを避ける
            if len(c)==0:
                raise ValueError('Empty Cluster')

        #クラスタを更新する　重心が変化しているかチェック
        converged = True
        for i in range(k):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print('iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print("")#空行を追加
    return clusters