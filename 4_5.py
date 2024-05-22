def factI(n):
    """n>0を整数と仮定
    n!を返す"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    """n>0を整数と仮定
    n!を返す"""
    if n == 1:
        return n
    else:
        return n * factR(n - 1)

