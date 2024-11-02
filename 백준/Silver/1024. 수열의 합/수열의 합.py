N, L = map(int, input().split())
flag = 0
for i in range(L, 101):
    n = (N - (i * (i - 1) // 2)) / i
    if n < 0:
        break
    if n == int(n):
        n = int(n)
        ans = list(range(n, n + i))
        flag = 1
        break
if flag:
    print(*ans)
else:
    print(-1)