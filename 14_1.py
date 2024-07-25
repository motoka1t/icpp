class Location(object):
    def __init__(self, x, y):
        """xとyは浮動小数点"""
        self.x, self.y = x, y
    
    def move(self, deltaX, deltaY):
        """deltaXとdeltaYは浮動小数点"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # Locationクラスのmoveメソッドを用いて、新しい位置情報を得る
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in Field')
        return self.drunks[drunk]