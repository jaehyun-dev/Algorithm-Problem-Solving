import math
N = int(input())
p = 4
for i in range(1, N + 1):
    p = int((math.sqrt(p) * 2 - 1) ** 2)
print(p)