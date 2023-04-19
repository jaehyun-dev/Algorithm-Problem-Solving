import sys
import collections
input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dq = collections.deque()
for j in range(N):
    for i in range(M):
        if graph[j][i] == 1:
            dq.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < M and 0 <= ny < N):
                continue
            if graph[ny][nx] == -1:
                continue
            if graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                dq.append((nx, ny))

bfs()
print(-1 if any(0 in row for row in graph) else max(max(row) for row in graph) - 1)