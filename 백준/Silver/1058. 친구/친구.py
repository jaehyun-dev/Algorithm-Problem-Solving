import sys
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'Y':
            graph[i][j] = 1
        else:
            graph[i][j] = 0

for k in range(N):
    for a in range(N):
        for b in range(N):
            if a != b and graph[a][k] != 0 and graph[k][b] != 0:
                if graph[a][b] == 0:
                    graph[a][b] = graph[a][k] + graph[k][b]
                else:
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if 1 <= graph[i][j] <= 2:
            cnt += 1
    if ans < cnt:
        ans = cnt
print(ans)