def minkowskiDest(v1, v2, p):
    """v1とv2は長さの等しい数値配列であるとする
       v1とv2の、p次のミンコウスキ距離を返す"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i]-v2[i])**p
    return dist**(1/p)