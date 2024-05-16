#完全立方に対する立方根を求める。
x = int(input('Enter an integer: '))
for ans in[0, abs(x)+1]:
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if ans < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)