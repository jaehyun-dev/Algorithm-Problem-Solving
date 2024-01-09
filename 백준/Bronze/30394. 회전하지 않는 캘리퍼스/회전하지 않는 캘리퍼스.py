import sys
input = sys.stdin.readline
N = int(input())
m = int(1e9)
M = int(-1e9)
for _ in range(N):
    x, y = map(int, input().split())
    if y < m:
        m = y
    if M < y:
        M = y
print(M - m)