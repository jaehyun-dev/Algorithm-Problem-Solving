n = int(input())
s = set()
cnt = 0
for i in range(1, int(n ** (1 / 2)) + 1):
    for j in range(1, n + 1):
        if i * j <= n and (j, i) not in s:
            s.add((i, j))
            cnt += 1
print(cnt)