import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    global area
    if vis[r][c] or not graph[r][c]:
        return False
    vis[r][c] = True
    area += 1
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc]:
            dfs(nr, nc)
    return True

M, N, K = map(int, input().split())
graph = [([1] * M) for _ in range(N)]
vis = [([False] * M) for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 0

cnt = 0
area = 0
a_list = []
for r in range(N):
    for c in range(M):
        area = 0
        if dfs(r, c):
            cnt += 1
            a_list.append(area)

print(cnt)
print(*sorted(a_list))