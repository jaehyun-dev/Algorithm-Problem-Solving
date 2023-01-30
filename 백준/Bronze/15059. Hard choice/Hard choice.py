a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans += max(b[i] - a[i], 0)
print(ans)