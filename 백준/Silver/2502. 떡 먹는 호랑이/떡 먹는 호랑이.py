D, K = map(int, input().split())
f = int(K // 1.618)
c = 0
while 1:
    flag = 1
    f -= c
    dp = [K, f]
    for i in range(D - 2):
        dp.append(dp[i] - dp[i + 1])
        if dp[-2] < dp[-1]:
            flag = 0
            break
    if flag:
        break
    if 0 < c:
        c += 1
    else:
        c -= 1
    c = -c
print(dp[-1])
print(dp[-2])