import sys
for line in sys.stdin:
    M, P, L, E, R, S, N = map(int, line.strip().split())
    n = 0
    while n < N:
        L, P, M = M * E, L // R, P // S
        n += 1
    print(M)