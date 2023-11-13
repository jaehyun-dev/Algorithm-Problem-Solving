import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    global area
    if vis[r][c] or graph[r][c] == 0:
        return False
    vis[r][c] = True
    area += 1
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1:
            dfs(nr, nc)
    return True

n, m = map(int, input().split())
graph = []
vis = [([False] * m) for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0
max_area = 0
for r in range(n):
    for c in range(m):
       area = 0
       if dfs(r, c):
           cnt += 1
           if max_area < area:
               max_area = area

print(cnt)
print(max_area)