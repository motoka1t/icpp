def intersect(L1, L2):
    """L1とL2をリストとする
    L1とL2の共通部分からなる、重複のないリストを返す"""
    #共通の要素からなるリストを構築する
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
                break
    #重複のないリストを構築する
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result