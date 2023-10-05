import sys
input = sys.stdin.readline
n, m = int(input()), int(input())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] == 0:
        graph[a][b] = c
    else:
        graph[a][b] = min(graph[a][b], c)
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                continue
            if graph[a][b] != 0 and graph[a][k] != 0 and graph[k][b] != 0:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            elif graph[a][b] == 0 and graph[a][k] != 0 and graph[k][b] != 0:
                graph[a][b] = graph[a][k] + graph[k][b]
for i in range(1, n + 1):
    print(*graph[i][1:])