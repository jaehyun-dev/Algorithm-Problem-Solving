import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = [0] * (N + 1)
for _ in range(M):
    b, c = map(int, input().split())
    a[b] += 1
    a[c] += 1
for i in range(1, N + 1):
    print(a[i])