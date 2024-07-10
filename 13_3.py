def maxVal(toConsider, avail):
    """toConsiderを品物のリスト、availを重さとする
    それらをパラメータとする0/1ナップザック問題の解である
    総価値と品物のリストからなるタプルを返す"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #右側の分岐のみを探索する
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #左側の分岐を探索する
        withVal, withToTake = maxVal(toConsider[:1], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #右側の分岐を探索する
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        #より良い分岐を選択
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
