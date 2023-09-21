import collections

def bfs(p):
    queue.append(p)
    while queue:
        p = queue.popleft()
        r = p[0]
        c = p[1]
        visited[r][c] = 1
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and graph[nr][nc] == 1:
                    graph[nr][nc] = graph[r][c] + 1
                    queue.append((nr, nc))

N, M = map(int, input().split())
graph = []
visited = []
for _ in range(N):
    visited.append([0] * M)
for _ in range(N):
    graph.append(list(map(int, input())))
queue = collections.deque()
bfs((0, 0))
print(graph[N - 1][M - 1])