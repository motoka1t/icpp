def clear(n, p, steps):
    """n と steps は正の整数、pは浮動小数点数
       n: 分子の初期個数
       p: 分子が消滅する確率
       steps: シミュレーションの長さ"""
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('Time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
    