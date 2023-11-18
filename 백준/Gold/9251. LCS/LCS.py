A = input()
B = input()
a = len(A)
b = len(B)
dp = [([0] * (a + 1)) for _ in range(b + 1)]

for i in range(b):
    for j in range(a):
        if B[i] == A[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
print(dp[b][a])