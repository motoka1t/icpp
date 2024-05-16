x = 25
epsilon = 0.01
step = epsilon**3
numGuess = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans * ans <= x:
    ans += step
    numGuess += 1
print('numGuess =', numGuess)
if (abs(ans**2 - x) >= epsilon):
    print('Failed on square root of', x)
else:
    print(ans, 'is close to root of', x)