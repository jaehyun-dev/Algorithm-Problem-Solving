import sys
input = sys.stdin.readline
N = int(input())
r = 0
for _ in range(N):
    s, a = map(int, input().split())
    r += a % s
print(r)