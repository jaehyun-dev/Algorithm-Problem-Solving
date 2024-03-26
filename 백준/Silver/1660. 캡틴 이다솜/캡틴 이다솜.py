import sys
input = sys.stdin.readline
N = int(input())
balls = []
b = 0
i = 1
while b < N:
    b += i * (i + 1) // 2
    balls.append(b)
    i += 1
dp = [sys.maxsize] * (N + 1)
for i in range(1, N + 1):
    for b in balls:
        if i <= b:
            if b == i:
                dp[i] = 1
            break
        dp[i] = min(dp[i], dp[i - b] + 1)
print(dp[N])