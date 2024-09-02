import pylab

class Cluster(object):
    def __init__(self, examples):
        """examplesはExampleの空でないリストとする"""
        self.examples = examples
        self.centroid = self.computeCentroid()

    def update(self, examples):
        """examplesはExampleの空でないリストとする
           examplesを更新し、重心の総量の変化を返す"""
        oldCentroid = self.centroid
        self.examples = examples
        self.centroid = self.computeCentroid()
        return oldCentroid.distance(self.centroid)
    
    def computeCentroid(self):
        vals = pylab.array([0.0]*self.examples[0].dimensionality())
        for e in self.examples: #平均を計算
            vals += e.getFeatures()
        centroid = Example('centroid', vals/len(self.examples))
        return centroid
    
    def getCentroid(self):
        return self.centroid
    
    def variability(self):
        totDist = 0.0
        for e in self.examples:
            totDist += (e.distance(self.centroid))**2
        return totDist
    
    def members(self):
        for e in self.examples:
            yield e

    def __str__(self):
        names = []
        for e in self.examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid ' + str(self.centroid.getFeatures()) + ' contains\n '
        for e in names:
            result = result + e + ','
        return result[:-2] #最後にあるコンマとスペースを取り除く    
