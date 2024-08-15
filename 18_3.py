from chapter18 import *
import pylab

def fitData(inputFile):
    masses, distances = getData(inputFile)
    distances = pylab.array(distances)
    forces = pylab.array(masses)*9.81
    pylab.plot(forces, distances, 'ko', label = 'Measured displacements')
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force|(Newtons)')
    pylab.ylabel('Distance(meters)')
    #１次の適合曲線（直線）を求める
    distances1 = pylab.array(distances[:-6])
    forces1 = pylab.array(masses[:-6])*9.81
    a,b = pylab.polyfit(forces1, distances1, 1)
    predictedDistances = a*pylab.array(forces1)+b
    k = 1.0/a #文中の説明を参照のこと
    pylab.plot(forces1, predictedDistances, label='Displacements predicted by\nlinear fit. k =' + str(round(k,5)))
    #3次の適合曲線を求める
    fit = pylab.polyfit(forces, distances, 3)
    predictedDistances = pylab.polyval(fit, forces)
    pylab.plot(forces, predictedDistances, 'k:', label='cobic fit')

    pylab.legend(loc='best')
    pylab.show()

fitData('springData.txt')