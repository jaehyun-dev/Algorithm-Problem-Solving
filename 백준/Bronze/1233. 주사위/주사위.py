S1, S2, S3 = map(int, input().split())
d = {}
for i in range(3, S1 + S2 + S3 + 1):
    d[i] = 0
for i in range(1, S1 + 1):
    for j in range(1, S2 + 1):
        for k in range(1, S3 + 1):
            d[i + j + k] += 1
M = 0
ans = 3
for i in d:
    if M < d[i]:
        M = d[i]
        ans = i
print(ans)