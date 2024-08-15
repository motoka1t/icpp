import random
treatmentDist = (119.5, 5.0)
controlDist = (120, 4.0)
sampleSize = 100
treatmentTimes, controlTimes = [], []
for s in range(sampleSize):
    treatmentTimes.append(random.gauss(treatmentDist[0], treatmentDist[1]))
    controlTimes.append(random.gauss(controlDist[0], controlDist[1]))