import pylab

def findPayment(loan, r, m):
    """loanとrをfloat型とし、mをint型とすr
    月割りの金利をrとして、借入額loanの住宅ローンを
    mヶ月で返済する場合の、毎月の偏在学を返す"""
    return loan * ( (r * (1 + r)**m) / ((1 + r)**m - 1))

class Mortgage(object):
    """異なる種類の住宅ローンを構築するための抽象クラス"""
    def __init__(self, loan, annRate, months):
        """loanとannRateをfloat型とし、monthsをint型とする
        借入額loan、返済月数months、年利annRateであるような
        住宅ローンを新たに生成する"""
        self.loan = loan
        self.rate = annRate/12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #住宅ローンの種類（サブクラスで用いる

    def makePayment(self):
        """返済を行う"""
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def getTotalPaid(self):
        """これまでに支払った総額を返す"""
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)

    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)

    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)

    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * len(self.outstanding))
        equityAcquired = equityAcquired - pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)

    
