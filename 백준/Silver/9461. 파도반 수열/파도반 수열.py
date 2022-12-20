import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 1, 1, 1, 2, 2]
    for i in range(6, n + 1):
        dp.append(dp[i - 1] + dp[i - 5])
    print(dp[n])