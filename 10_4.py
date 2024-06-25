def merge(left, right, compare):
    """leftとrightをソートずみのリストとし
    compareを要素官の順序を定義する関数とする
    （left + right)と同じ要素からなり
    compareに従いソートされた新たなリストを返す"""
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L, compare = lambda x,y: x<y):
    """Lをリストとし
    compareをLの要素間の順序を定義する関数とする
    Lと同じ要素からなり、ソートされた新たなリストを返す"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len[L]/2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)
