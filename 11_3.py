from mortgage import*


def compareMortgage(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts =[fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayments()
    plotMortgage(morts, amt)
