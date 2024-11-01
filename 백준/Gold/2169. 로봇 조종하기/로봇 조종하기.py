import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [None] * N
for i in range(N):
    graph[i] = list(map(int, input().split()))
dp = [([([0, 0, 0]) for _ in range(M)]) for _ in range(N)]
dp[0][0] = [graph[0][0]] * 3
for j in range(1, M):
    dp[0][j] = [dp[0][j - 1][0] + graph[0][j]] * 3
for i in range(1, N):
    for j in range(M):
        dp[i][j][2] = max(dp[i - 1][j]) + graph[i][j]
        dp[i][M - 1 - j][2] = max(dp[i - 1][M - 1 - j]) + graph[i][M - 1 - j]
        if j == 0:
            dp[i][j][1] = dp[i][j][2]
            dp[i][M - 1 - j][0] = dp[i][M - 1 - j][2]
        else:
            dp[i][j][1] = max(dp[i][j - 1][1], dp[i][j - 1][2]) + graph[i][j]
            dp[i][M - 1 - j][0] = max(dp[i][M - j][0], dp[i][M - j][2]) + graph[i][M - 1 - j]
print(max(dp[N - 1][M - 1]))