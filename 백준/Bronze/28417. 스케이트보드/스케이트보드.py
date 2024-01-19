import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for _ in range(N):
    a = list(map(int, input().split()))
    r = max(a[:2])
    t = sum(sorted(a[2:], reverse=True)[:2])
    s = r + t
    if ans < s:
        ans = s
print(ans)