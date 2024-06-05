N = int(input())
d = {}
for i in range(N):
    d[i] = int(input())
ans = 0
M = int(input())
for _ in range(M):
    ans += d[int(input()) - 1]
print(ans)