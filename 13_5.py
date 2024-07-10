def fastMaxVal(toConsider, avail, memo={}):
    """toConsiderを品物のリスト、availを重さ
    memoは再帰呼び出しによってのみ使われるとする
    それらをパラメータとする0/1ナップザック問題の解である
    総価値と品物のリストからなるタプルを返す"""
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider.getWeight() > avail:
        #右側の分岐のみを探索する
        result = fastMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        #左側の分岐を探索する
        withVal, withToTake = fastMaxVal(toConsider[1:], avail-nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        #右側の分岐を探索する
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:], avail ,memo)
        #より良い分岐を選択
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem, ))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result


    