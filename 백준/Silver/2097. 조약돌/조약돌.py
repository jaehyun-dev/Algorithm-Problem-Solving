import math
N = int(input())
if N <= 4:
    print(4)
else:
    a = int(math.sqrt(N))
    if N <= a ** 2:
        print((a - 1)  * 4)
    elif N <= a * (a + 1):
        print((2 * a - 1) * 2)
    else:
        print(a * 4)