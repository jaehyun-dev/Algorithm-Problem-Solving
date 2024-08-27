import sys
import queue
input = sys.stdin.readline
n = int(input())
e = [0] * n
s = [0] * n
M = 0
for i in range(n):
    l = list(map(int, input().split()))
    m, se = l[0], l[1:]
    e[i] = m
    s[i] = max(se)
    if M < s[i]:
        M = s[i]
cnt = 0
for i in range(n):
    cnt += (M - s[i]) * e[i]
print(cnt)