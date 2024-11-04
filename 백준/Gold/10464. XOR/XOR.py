import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    S, F = map(int, input().split())
    c = (F - S) % 4
    if S % 2:
        dp = [S] + [0] * 3
        for i in range(min(3, F - S)):
            dp[i + 1] = dp[i] ^ (F - c + 1 + i)
    else:
        dp = [0, 1, 0, 0]
        dp[0] = F - c
        dp[2] = 1 ^ (F - c + 2)
    print(dp[c])