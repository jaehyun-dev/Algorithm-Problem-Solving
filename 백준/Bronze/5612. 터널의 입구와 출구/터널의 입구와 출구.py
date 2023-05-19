import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
M = m
cur = m
flag = True
for _ in range(n):
    if cur < 0:
        print(0)
        flag = False
        break
    a, b = map(int, input().split())
    cur = cur + a - b
    M = max(M, cur)
if flag:
    print(M)