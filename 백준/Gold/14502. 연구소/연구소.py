import sys, itertools
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(r, c, graph, vis):
    global cnt
    if graph[r][c] == 1 or vis[r][c]:
        return
    vis[r][c] = 1
    if graph[r][c] == 0:
        cnt -= 1
    graph[r][c] = 2
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            dfs(nr, nc, graph, vis)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
space = []
virus = []
cnt_o = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] == 0:
            space.append((r, c))
            cnt_o += 1
        elif graph[r][c] == 2:
            virus.append((r, c))
ans = 0
for case in itertools.combinations(space, 3):
    cnt = cnt_o
    temp = []
    for i in range(N):
        temp.append(list(graph[i]))
    vis = [[0] * M for _ in range(N)]
    for r, c in case:
        temp[r][c] = 1
    for r, c in virus:
        dfs(r, c, temp, vis)
    if ans < cnt:
        ans = cnt

print(ans - 3)