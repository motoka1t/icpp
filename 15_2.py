def flip(numFlips):
    """numFlips: 正の整数"""
    heads = 0
    for i in range(numFlips):
        if random.choice(['H', 'T']) == 'H':
            heads += 1
    return heads/numFlips

def flipSim(numFlipsPerTrial, numTrials):
    """numFlipsPerTrial, numTrials: 正の整数"""
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/len(fracHeads)
    return mean
