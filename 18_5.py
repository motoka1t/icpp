def rSquared(measured, predicted):
    """measerdは観測値を保持する1次元の配列
       predictedは予測値を保持する1次元の配列を仮定する
       決定係数を返す"""
    estimateError = ((predicted - measured)**2).sum()
    meanOfMeasured = measured.sum()/len(measured)
    variability = ((measured - meanOfMeasured)**2).sum()
    return 1 - estimateError/variability
