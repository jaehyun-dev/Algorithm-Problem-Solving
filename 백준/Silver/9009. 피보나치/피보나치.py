T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0, 1]
    i = 2
    while 1:
        a = dp[i - 2] + dp[i - 1]
        if n < a:
            break
        dp.append(a)
        i += 1
    s = n
    l = []
    i -= 1
    while 0 < s:
        m = dp[i]
        if m <= s:
            s -= m
            l.append(m)
        i -= 1
    print(*reversed(l))