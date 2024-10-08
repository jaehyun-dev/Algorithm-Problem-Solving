N = int(input())
dp = [([0] * 2) for _ in range(N)]
dp[0] = [1, 1]
for i in range(1, N):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] * 2) % 9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % 9901
print((dp[-1][0] + dp[-1][1] * 2) % 9901)