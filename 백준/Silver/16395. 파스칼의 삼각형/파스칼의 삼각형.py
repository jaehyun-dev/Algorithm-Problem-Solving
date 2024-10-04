n, k = map(int, input().split())
if n < 3:
    print(1)
else:
    l = [([0] * n) for _ in range(n)]
    for i in range(n):
        l[i][0] = l[i][i] = 1
    for i in range(2, n):
        for j in range(1, n - 1):
            l[i][j] = l[i - 1][j -1] + l[i -1][j]
    print(l[n - 1][k - 1])