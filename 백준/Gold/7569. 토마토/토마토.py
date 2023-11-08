import sys, collections
input = sys.stdin.readline

def bfs():
    ans = 0
    q = collections.deque()
    for t in tomato:
        q.append(t)
    while q:
        h, r, c, d = q.popleft()
        for dh, dr, dc in ((-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)):
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and not vis[nh][nr][nc] and graph[nh][nr][nc] == 0:
                vis[nh][nr][nc] = True
                graph[nh][nr][nc] = 1
                q.append([nh, nr, nc, d + 1])
                ans = max(ans, d + 1)
    return ans

M, N, H = map(int, input().split())
graph = []
tomato = []
vis = [([([False] * M) for _ in range(N)]) for _ in range(H)]
for h in range(H):
    floor = []
    for n in range(N):
        floor.append(list(map(int, input().split())))
        for m in range(M):
            if floor[n][m] == 1:
                tomato.append([h, n, m, 0])
    graph.append(floor)
ans = bfs()
flag = False
for h in range(H):
    for r in range(N):
        for c in range(M):
            if graph[h][r][c] == 0:
                flag = True
                break
        if flag:
            break
    if flag:
        break
print(-1 if flag else ans)