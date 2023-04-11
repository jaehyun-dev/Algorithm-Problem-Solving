import sys
input = sys.stdin.readline
X, Y = map(int, input().split())
p = X / Y * 1000
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    p = min(p, X / Y * 1000)
print(p)