N = int(input())
ans = 0
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(N):
        ans += a[j]
print(ans)