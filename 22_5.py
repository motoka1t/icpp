import pylab

class Animal(object):
    def __init__(self, name, feature):
        """nameは文字列、featureは数値のリストとする"""
        self.name = name
        self.feature =feature
    
    def getName(self):
        return self.name
    
    def getFeature(self):
        return self.feature
    
    def distance(self, other):
        """otherはAnimalオブジェクトとする
        自分自身とotherの間のユークリッド距離を返す"""
        return minkowskiDist(self.getFeature(), other.getFeature(), 2)