n = int(input())
dp = [0, 1, 2] + [0 for _ in range(n - 2)]
if n < 3:
    print(dp[n])
else:
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[n] % 10007)