n = int(input())
m = float("inf")
for i in range(1, int(n ** (1 / 3)) + 2):
    for j in range(1, int(n ** (1 / 2)) + 2):
        k = n / i / j
        if k == int(k):
            k = int(k)
            s = 2 * (i + j + k)
            if s < m:
                m = s
                ans = [i, j, k]
print(*ans)