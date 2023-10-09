import sys
input = sys.stdin.readline
N = int(input())
dp = list(map(int, input().split()))
for _ in range(N - 1):
    a = list(map(int, input().split()))
    dp = [min(dp[1], dp[2]) + a[0], min(dp[0], dp[2]) + a[1], min(dp[0], dp[1]) + a[2]]
print(min(dp))