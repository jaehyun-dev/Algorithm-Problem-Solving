N = int(input())
ans = 10000
for _ in range(N):
    r, q = map(int, input().split())
    if q // r < ans:
        ans = q // r
print(ans)