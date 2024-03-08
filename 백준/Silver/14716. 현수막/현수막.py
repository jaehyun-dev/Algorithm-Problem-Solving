import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    if vis[r][c] or graph[r][c] == 0:
        return False
    vis[r][c] = 1
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 1 and not vis[nr][nc]:
            dfs(nr, nc)
    return True

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))
vis = [([0] * N) for _ in range(M)]
cnt = 0
for r in range(M):
    for c in range(N):
        if dfs(r, c):
            cnt += 1
print(cnt)