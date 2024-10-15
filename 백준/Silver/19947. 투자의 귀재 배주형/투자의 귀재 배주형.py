H, Y = map(int, input().split())
l = max(Y + 1, 6)
dp = [0] * l
dp[0] = H
for i in range(1, 3):
    dp[i] = int(dp[i - 1] * 1.05)
for i in range(3, 5):
    dp[i] = int(max(dp[i - 1] * 1.05, dp[i - 3] * 1.2))
for i in range(5, l):
    dp[i] = int(max(dp[i - 1] * 1.05, dp[i - 3] * 1.2, dp[i - 5] * 1.35))
print(dp[Y])