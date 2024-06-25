class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible___ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directry'

    def printVisible(self):
        print(self.visible)
    
    def printInvisible(self):
        print(self.__invisible)
    
    def __printInvisible(self):
        print(self.__invisible)

    def __printInvisible__(self):
        print(self.__invisible)
