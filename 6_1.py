def isPal(x):
    """xをリストとする
    そのリストが回文ならTrueを、そうでなkればFalseを返す"""
    tenp = x[:]
    tenp.reverse()
    if tenp == x:
        return True
    else:
        return False
    
def silly(n):
    """nを正のint型とする
    ユーザからn個の入力を受け付ける
    もし入力文字列が回文であれば'YES'を
    そうでなkれば'No'を出力する"""
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
