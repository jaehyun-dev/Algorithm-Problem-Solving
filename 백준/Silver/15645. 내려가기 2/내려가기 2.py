import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dp = [[(graph[0]) for _ in range(2)]]
for i in range(N - 1):
    dp.append([([0] * 3) for _ in range(2)])
    dp[i + 1][0][0] = max(dp[i][0][:2]) + graph[i + 1][0]
    dp[i + 1][0][1] = max(dp[i][0]) + graph[i + 1][1]
    dp[i + 1][0][2] = max(dp[i][0][1:]) + graph[i + 1][2]
    dp[i + 1][1][0] = min(dp[i][1][:2]) + graph[i + 1][0]
    dp[i + 1][1][1] = min(dp[i][1]) + graph[i + 1][1]
    dp[i + 1][1][2] = min(dp[i][1][1:]) + graph[i + 1][2]
print(max(dp[-1][0]), min(dp[-1][1]))