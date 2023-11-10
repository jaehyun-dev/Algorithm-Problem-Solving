import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, c, h):
    if vis[r][c] or graph[r][c] <= h:
        return False
    vis[r][c] = True
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, h)
    return True

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
max_height = max(max(row) for row in graph)
ans = 1
for h in range(1, max_height):
    vis = [([False] * N) for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if dfs(r, c, h):
                cnt += 1
    if ans < cnt:
        ans = cnt

print(ans)