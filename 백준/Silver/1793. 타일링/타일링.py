import sys
for l in sys.stdin:
    n = int(l.strip())
    if n == 0:
        print(1)
        continue
    elif n == 1:
        print(1)
        continue
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
    print(dp[n])