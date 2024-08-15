def calcBayes(priorA, probBifA, probB):
    """priorA: 事象Aの事前確率でBとは独立
       probBifA: Aが与えられた条件付きのBの確率
       probB: 事象Bの確率
       Bが与えられた条件下で事象Aを得る事後確率が結果として戻される"""
    return priorA*probBifA/probB

priorA = 1/3
prob6ifA = 1/5
prob6 = (1/5 + 1/6 + 1/7)/3

postA = calcBayes(priorA, prob6ifA, prob6)
print('タイプAである確率 =', round(postA, 4))
postB = calcBayes(postA, prob6ifA, prob6)
print('タイプAである確率 =', round(postB, 4))