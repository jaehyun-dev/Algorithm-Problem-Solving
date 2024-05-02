C, K, P = map(int, input().split())
ans = 0
for n in range(1, C + 1):
    ans += n * (K + P * n)
print(ans)