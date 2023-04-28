import math
N = int(input())
i = int(math.sqrt(N))
if i * i >= N:
    print(i, i)
elif i * (i + 1) >= N:
    print(i, i + 1)
else:
    print(i + 1, i + 1)