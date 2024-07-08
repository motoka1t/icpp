from mortgage import *
import pylab

def plotMortgage(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(lot = 'best')
    styles = ['k-', 'k-.', 'k:']
    #図を指定する際、番号の代わりに名前を用いる
    payments, cost, balance, netCost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])

    labelPlot(payments, 'Monthly Payment of $' + str(amt) + ' Mortgages', 'Months', 'Monthly Payments')
    labelPlot(cost, 'Cash Outlay of $' + str(amt) + ' Mortgage', 'Months', 'Tota lPayments')
    labelPlot(balance, 'Balance Remaining of $' + str(amt) + ' Mortgage', 'Months', 'Remaining Loan Balance of $')
    labelPlot(netCost, 'Nest Cost of $' + str(amt) + ' Mortgage', 'Months', 'Payments - Equity $')
    pylab.show()