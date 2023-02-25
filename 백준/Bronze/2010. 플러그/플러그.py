import sys
input = sys.stdin.readline
N = int(input().strip())
ans = 0
for _ in range(N):
    a = int(input().strip())
    ans += a
print(ans - N + 1)