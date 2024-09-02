def zScaleFeatures(vals):
    """valsはfloatの列とする"""
    result = pylab.array(vals)
    mean = sum(result)/len(result)
    result = result - mean
    return result/stdDev(result)

def iScaleFeatures(vals):
    """valsはfloatの列とする"""
    minVal, maxVal = min(vals), max(vals)
    fit = pylab.polyfit([minVal, maxVal], [0,1], 1) 
    return pylab.polyval(fit, vals)  