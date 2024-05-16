N, K = map(int, input().split())
ans = 0
l = []
for x in range(1, N + 1):
    if x % 10 != K % 10 and x % 10 != 2 * K % 10:
        ans += 1
        l.append(x)
print(ans)
print(*l)