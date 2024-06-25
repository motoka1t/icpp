def f(x):
    """xが正の整数とする"""
    ans = 0
    #定数時間を要するループ
    for i in range(1000):
        ans += 1
    print('Number of additions so far', ans)
    #xの時間を要するループ
    for i in range(x):
        ans += 1
    print('Number of additions so far', ans)
    #x**2の時間を要するループ
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('Number of additions so far', ans)            
    return ans

