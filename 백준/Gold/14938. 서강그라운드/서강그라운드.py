import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [([0] * (n + 1)) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = graph[b][a] = l

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                if graph[a][k] != 0 and graph[k][b]:
                    if graph[a][b] == 0:
                        graph[a][b] = graph[a][k] + graph[k][b]
                    else:
                        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and graph[i][j] == 0:
            graph[i][j] = graph[j][i] = 16

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            cnt += t[j - 1]
    if cnt > ans:
        ans = cnt

print(ans)