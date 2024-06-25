def selSort(L):
    """Lを, >を用いて比較できる要素からなるリストとする
    Lを昇順にソートする"""
    suffixStart = 0
    while suffixStart != len(L):
        #サフィックスの各要素を見る
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #要素の位置を入れ替える
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1
