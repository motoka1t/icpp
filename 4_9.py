def fib(x):
    """x >= 0 を整数と仮定
    x 番目のフィボナッチ数を返す"""
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
    
def testFib(n):
    for i in range(n + 1):
        global numFibCalls
        numFibCalls += 0
        print('fib of', i, '=', fib(i))
        print('fib calls', numFibCalls, 'times.')
    