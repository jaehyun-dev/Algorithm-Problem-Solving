N = int(input())
A = list(map(int, input().split()))
dp = [0] * (N + 1)
ans = 0
for i in range(1, N + 1):
    idx = 0
    for j in range(i):
        if A[j - 1] < A[i - 1] and dp[idx] < dp[j]:
            idx = j
    dp[i] = dp[idx] + 1
    if ans < dp[i]:
        ans = dp[i]
print(ans)