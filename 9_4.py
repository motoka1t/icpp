def isSubset(L1, L2):
    """L1とL2をリストとする
    L1の各要素がL2にもあればTrueを
    そうでなければFalseを返す"""
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
            if not matched:
                return False
        return True
