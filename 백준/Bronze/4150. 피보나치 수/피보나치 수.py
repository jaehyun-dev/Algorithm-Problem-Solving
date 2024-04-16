N = int(input())
dp = [0] * max(N, 2)
dp[0] = dp[1] = 1
for i in range(2, N):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[N - 1])