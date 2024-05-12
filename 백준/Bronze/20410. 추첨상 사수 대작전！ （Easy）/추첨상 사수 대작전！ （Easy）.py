m, Seed, X1, X2 = map(int, input().split())
flag = 0
for a in range(m):
    for c in range(m):
        if X1 == (a * Seed + c) % m and X2 == (a * X1 + c) % m:
            ans = [a, c]
            flag = 1
            break
    if flag:
        break
print(*ans)