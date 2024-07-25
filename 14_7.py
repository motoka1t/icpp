def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0,0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = sum(xVals)/len(xVals)
        meanY = sum(yVals)/len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__+'mean loc. =<'+str(meanX)+','+str(meanY)+'>')
    pylab.title('Location end of Walks (' + str(numSteps) + 'steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/Sourth of Origin')
    pylab.legend(loc ='lower left')

plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)
