from factorial import *
from fibonacci import *

def applyToEach(L, f):
    """Lをリストとし、fを関数とする。
    Lのそれぞれの要素eをf(e)に置き換えてLを更新する。"""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('Apply abs to each element of L.')
applyToEach(L, abs)
print('Apply int to each element of', L)
applyToEach(L, int)
print('L =', L)
print('Apply factorial to each element of', L)
applyToEach(L, factR)
print('Apply fibonacci to each element of', L)
applyToEach(L, fib)