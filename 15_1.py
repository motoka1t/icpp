import random

def rollDie():
    """1から6までの整数を無作為に選んで返す"""
    return random.choice([1,2,3,4,5,6])

def rollN(n):
    result = ''
    for i in range(n):
        result = result + str(rollDie()) 
    print(result)
