def accuracy(truePos, falsePos, trueNeg, falseNeg):
    numerater = truePos + falsePos
    denominator = truePos + falsePos + trueNeg + falseNeg
    return numerater / denominator

def sensitivity(truePos, falseNeg):
    try:
        return truePos/(truePos+falseNeg)
    except ZeroDivisionError:
        return float('nan')   

def specificity(trueNeg, falsePos):
    try:
        return trueNeg/(trueNeg+falsePos)
    except ZeroDivisionError:
        return float('nan')    

def posPredVal(truePos, falsePos):
    try:
        return truePos/(truePos+falsePos)
    except ZeroDivisionError:
        return float('nan')

def negPredVal(trueNeg, falseNeg):
    try:
        return trueNeg/(trueNeg+falseNeg)
    except ZeroDivisionError:
        return float('nan')
    
def getStats(truePos, falsePos, trueNeg, falseNeg, toPoint=True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if toPoint:
        print(' Accuracy =', round(accur, 3))
        print(' Sensitivity =', round(sens, 3))
        print(' Specificity =', round(spec, 3))
        print(' Positive Predictive Value =', round(ppv,3))
    return (accur, sens, spec, ppv)