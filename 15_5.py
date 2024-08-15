def variance(X):
    """Xを数のリストとする
    Xの分散を返す"""
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    return tot/len(X)

def stdDev(X):
    """Xを数のリストとする
    Xの標準偏差を返す"""
    return variance(X)**0.5
