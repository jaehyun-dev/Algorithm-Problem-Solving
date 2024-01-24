import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int, input().split()))
p = 0
ans = 0
i = 0
while i < N:
    h = H[i]
    if p <= h:
        ans += 1
    p = h
    i += 1
print(ans)