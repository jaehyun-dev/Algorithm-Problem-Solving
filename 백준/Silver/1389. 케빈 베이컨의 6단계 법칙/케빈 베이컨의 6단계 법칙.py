import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [([M + 1] * (N + 1)) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
                temp = graph[a][k] + graph[k][b]
                graph[a][b] = min(graph[a][b], temp)
cnt = N ** 2
ans = 0
for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        temp += graph[i][j]
    if temp < cnt:
        cnt = temp
        ans = i
print(ans)