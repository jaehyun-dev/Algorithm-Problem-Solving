import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global cnt
    if visited[r][c] or graph[r][c] == 'X':
        pass
    elif graph[r][c] in ['I', 'O', 'P'] and not visited[r][c]:
        visited[r][c] = True
        if graph[r][c] == 'P':
            cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                dfs(nr, nc)


N, M = map(int, input().split())
graph = []
visited = []
for _ in range(N):
    graph.append(list(input().strip()))
    visited.append([False] * M)
cnt = 0
flag = False
for r in range(N):
    for c in range(M):
        if graph[r][c] == 'I':
            flag = True
            break
    if flag:
        break
dfs(r, c)
print(cnt if cnt > 0 else 'TT')