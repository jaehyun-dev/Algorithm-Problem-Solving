import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, c):
    global vis
    if not (0 <= r < h and 0 <= c < w and not vis[r][c] and graph[r][c] == 1):
        return False
    vis[r][c] = True
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
        nr = r + dr
        nc = c + dc
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