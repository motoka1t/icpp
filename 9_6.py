def getBinaryRep(n, numDigits):
    """nとnumDigitsを非負のint型とする
    nの値を、numDigits桁の2新数で表す文字列を返す"""
    result = ""
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result

def genPowerset(L):
    """Lをリストとする
    Lの要素の、すべての可能な組み合わせからなるリストを返す
    例えば、Lが[1,2]ならば
    []、[1]、[2]、[1,2]"""
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] =='1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset