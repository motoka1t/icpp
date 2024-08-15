import pylab
import math

def createData(f, xVals):
    """fを引数を1つ取る関数とする
       xValsをfの引数の配列とする
       xValsの要素にfを適用した結果を保管した配列を返す"""
    yVals = []
    for i in xVals:
        yVals.append(f(xVals[i]))
    return pylab.array(yVals)

def fitExpData(xVals, yVals):
    """xValsとyValsを
       yVals[i] == f(xVals[i])となる数を保持する配列を仮定する
       ただし、fは指数関数とする
       log(f(x), base) == ax+bを満たすa,bを返す"""
    logVals = []
    for y in yVals:
        logVals.append(math.log(y, 2.0)) #底が2の対数を得る
    fit = pylab.polyfit(xVals, logVals, 1)
    return fit , 2.0

xVals = range(10)
f = lambda x: 3**x +x
yVals = createData(f, xVals)
pylab.plot(xVals, yVals, 'ko', label = 'Actual values')
fit, base = fitExpData(xVals, yVals)
predictedYVals = []
for x in xVals:
    predictedYVals.append(base**pylab.polyval(fit, x))
pylab.plot(xVals, predictedYVals, label = 'Predicted values')
pylab.title('Fitting an Exponential Function')
pylab.legend(loc = 'upper left')
pylab.show()
#オリジナルにはないxの値を求める
print('f(20)=', f(20))
print('Predicted value =', int(base**(pylab.polyval(fit,[20]))))