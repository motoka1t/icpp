class Node(object):
    def __init__(self, name):
        """nameは文字列とする"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        """srcとdestはどちらもNodeオブジェクトとする"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
    
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 0.0):
        """srcとdestはNodeオブジェクトとし、weightは数とする"""
        self.src = src
        self.dest = dest
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) +')' + self.dest.getName()