import random
def anyProb(numTrials):
    anyMonth48 = 0
    for trial in range(numTrials):
        months = [0]*12
        for i in range(446):
            months[random.randint(0,11)]+=1
        if max(months) >= 48:
            anyMonth48+=1
    aProb = round(anyMonth48/numTrials, 4)
    print('Probability of at least 48 births in same month =', aProb)