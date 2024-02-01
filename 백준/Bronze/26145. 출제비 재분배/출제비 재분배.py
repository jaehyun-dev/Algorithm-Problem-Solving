import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = list(map(int, input().split()))
S += [0] * M
for i in range(N):
    T = list(map(int, input().split()))
    S[i] -= sum(T)
    for j in range(N + M):
        S[j] += T[j]
print(*S)