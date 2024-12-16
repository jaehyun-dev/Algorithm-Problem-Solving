import sys
for line in sys.stdin:
    N, B, M = map(float, line.strip().split())
    i = 0
    while N <= M:
        N *= (1 + B / 100)
        i += 1
    print(i)