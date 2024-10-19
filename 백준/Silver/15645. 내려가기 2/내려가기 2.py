import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int, input().split()))
dp = [list(l), list(l)]
for _ in range(N - 1):
    t = list(map(int, input().split()))
    dp[0][0], dp[0][1], dp[0][2], dp[1][0], dp[1][1], dp[1][2] = max(dp[0][:2]) + t[0], max(dp[0]) + t[1], max(dp[0][1:]) + t[2], min(dp[1][:2]) + t[0], min(dp[1]) + t[1], min(dp[1][1:]) + t[2]
print(max(dp[0]), min(dp[1]))