import pylab

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials)/len(trials)
        meanDistances.append(mean)
    return meanDistances

def simAll(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyles()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label=dClass.__name__)
        pylab.title('Mean Distance from Origin (' + str(numTrials) + 'trials)')
        pylab.xlabel('Number of Steps')
        pylab.ylabel('Distance from Origin')
        pylab.legend(loc = 'best')
        pylab.semilogx()
        pylab.semilogy()

simAll((UsualDrunk, ColdDrunk, EWDrunk), (10,100,1000,10000,100000), 100)
