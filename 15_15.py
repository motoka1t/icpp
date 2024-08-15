import random

def simInsertions(numIndices, numInsertions):
    """numIndicesとnumInsertionsは正の整数
       衝突が起これば1、そうでなければ0を出力する"""
    choices = range(numIndices) #list of possible indices
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: # there is a collision
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions = 0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions / numTrials
