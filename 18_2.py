from chapter18 import *
import pylab

def plotData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    masses = pylab.array(masses)
    forces = masses*9.81
    pylab.plot(forces, distances, 'bo', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel("|Force|(Newtons)")
    pylab.ylabel('Distance(meters)')
    pylab.show()

plotData('springData.txt')
