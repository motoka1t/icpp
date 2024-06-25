from mitperson import *

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
 
    def getClass(self):
        return self.year

class Grad(Student):
    pass
