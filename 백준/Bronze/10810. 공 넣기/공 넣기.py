import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for l in range(i - 1, j):
        a[l] = k
print(*a)