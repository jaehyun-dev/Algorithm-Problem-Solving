import sys
input = sys.stdin.readline
N = int(input())
dp = [0, 0, 0]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp[0] = min(a[1], a[2]) + b[0]
dp[1] = min(a[0], a[2]) + b[1]
dp[2] = min(a[0], a[1]) + b[2]
for _ in range(N - 2):
    c = list(map(int, input().split()))
    temp = list(dp)
    temp[0] = min(dp[1], dp[2]) + c[0]
    temp[1] = min(dp[0], dp[2]) + c[1]
    temp[2] = min(dp[0], dp[1]) + c[2]
    dp = list(temp)
print(min(dp))