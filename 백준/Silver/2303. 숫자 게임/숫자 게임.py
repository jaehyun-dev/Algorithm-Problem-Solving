N = int(input())
M = 0
ans = 0
for n in range(N):
    l = list(map(int, input().split()))
    m = 0
    for i in range(3):
        for j in range(i + 1, 4):
            for k in range(j + 1, 5):
                m = max(m, (l[i] + l[j] + l[k]) % 10)
    if M <= m:
        ans = n + 1
        M = m
print(ans)