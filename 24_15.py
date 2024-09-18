def summarizeStats(stats):
    """statsは、正確度(accuracy)、感度(sensitivity)、
       特異度(specificity)、陽性的中率(pos. pred. val)、ROC
       の５つの浮動小数点のリストからなると仮定する"""
    def printStat(X, name):
        mean = round(sum(X)/len(X), 3)
        std = stdDev(X)
        print(' Mean', name, '=', str(mean) + ',', '95% confidence interval =', round(1.96*std, 3))
        accs, sens, specs, ppvs, aurocs = [], [], [], [], []
        for stat in stats:
            accs.append(stat[0])
            sens.append(stat[1])
            specs.append(stat[2])
            ppvs.append(stat[3])
            aurocs.append(stat[4])
        printStat(accs, 'accuracy')
        printStat(sens, 'sensitivity')
        printStat(specs, 'specificity')
        printStat(ppvs, 'pos. pred. val.')
        printStat(aurocs, 'AUROC')