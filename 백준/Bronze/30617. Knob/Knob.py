import sys
input = sys.stdin.readline
T = int(input())
ans = 0
pl, pr = (2, 2)
for _ in range(T):
    l, r = map(int, input().split())
    if l == r and l != 0:
        ans += 1
    if pl == l and l != 0:
        ans += 1
    if pr == r and r != 0:
        ans += 1
    pl, pr = l, r
print(ans)