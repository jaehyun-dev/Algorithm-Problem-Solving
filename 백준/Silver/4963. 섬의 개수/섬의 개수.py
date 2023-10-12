import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, c):
    if vis[r][c] or graph[r][c] == 0:
        return False
    vis[r][c] = True
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < h and 0 <= nc < w:
            dfs(nr, nc)
    return True

while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    graph = []
    vis = [[False] * w for _ in range(h)]
    cnt = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    for r in range(h):
        for c in range(w):
            if dfs(r, c):
                cnt += 1
    print(cnt)