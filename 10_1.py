def search(L, e):
    """Lを、要素が照準で並んだリストとする
    eがLにあればTrueを、そうでなければFalseを返す"""
    for i in range(len(L)):
        if L[i] ==e:
            return True
        if L[i] > e:
            return False
    return False