N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [0] * (N + 1)
for i in range(N):
    for j in range(i + arr[i][0], N + 1):
        dp[j] = max(dp[j], dp[i] + arr[i][1])
print(dp[N])