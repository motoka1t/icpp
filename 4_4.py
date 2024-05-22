def findRoot(x, power, epsilon):
    """xとepsilon>0は整数もしくは浮動小数点数、power>=1を整数と仮定
    y**powerがxのepsilon以内になるような浮動小数点数yを返す
    もし、そのような浮動小数点数が存在しなければ、Noneを返す"""
    if x < 0 and power%2 == 0:
        return None
    low = min(-1.0, x)
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans

def testFindRoot():
    epsilon = 0.0001
    for x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ', str(x), 'and power = ', power)
            result = findRoot(x, power, epsilon)
            if result == None:
                print('No Root')
            else:
                print(' ', result**power, '~=', x)    