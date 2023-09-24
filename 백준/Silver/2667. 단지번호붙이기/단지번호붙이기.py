def dfs(r, c):
    global n
    if visited[r][c] or graph[r][c] == 0:
        return False
    else:
        visited[r][c] = True
        n += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc] == 1:
            dfs(nr, nc)
    return True

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
visited = []
for _ in range(N):
    visited.append([False] * N)
house = []
for i in range(N):
    for j in range(N):
        n = 0
        if dfs(i, j):
            house.append(n)
print(len(house))
for i in sorted(house):
    print(i)