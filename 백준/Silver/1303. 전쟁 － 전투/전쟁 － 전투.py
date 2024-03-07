import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    global cnt_b
    global cnt_w
    global prev
    if prev == '':
        prev = graph[r][c]
    if vis[r][c] or graph[r][c] != prev:
        return False
    vis[r][c] = 1
    if graph[r][c] == 'W':
        cnt_w += 1
    else:
        cnt_b += 1
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < M and 0 <= nc < N and not vis[nr][nc]:
            dfs(nr, nc)
    return True

N, M = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(input().strip()))
vis = [([0] * N) for _ in range(M)]
ttl_w = 0
ttl_b = 0
for r in range(M):
    for c in range(N):
        prev = ''
        cnt_w = 0
        cnt_b = 0
        if dfs(r, c):
            ttl_w += cnt_w ** 2
            ttl_b += cnt_b ** 2
print(ttl_w, ttl_b)