import sys
input = sys.stdin.readline
N = int(input())
d = {}
for _ in range(N):
    f, n = input().split()
    if f in d:
        d[f] += int(n)
    else:
        d[f] = int(n)
flag = 1
for f in d:
    if d[f] == 5:
        flag = 0
        break
print("NO" if flag else "YES")