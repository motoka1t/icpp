def fastFib(n, memo = {}):
    """nを0以上の整数とする。memoは再起呼び出しによってのみ使われる
    n番目のフィボナッチ数を返す"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    