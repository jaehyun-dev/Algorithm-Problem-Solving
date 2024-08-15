import sys
input = sys.stdin.readline
U, N = map(int, input().split())
d = {}
for i in range(1, U + 1):
    d[i] = []
for _ in range(N):
    S, P = input().split()
    d[int(P)].append(S)
m = N
p = 0
for i in d:
    if 0 < len(d[i]) < m:
        m = len(d[i])
        p = i
print(d[p][0], p)