import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(r, c):
    global cnt
    if visited[r][c] or not graph[r][c]:
        return False
    visited[r][c] = 1
    cnt += 1
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            dfs(nr, nc)
    return True

N, M, K = map(int, input().split())
graph = [([0] * M) for _ in range(N)]
visited = [([0] * M) for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = 1
ans = 0
for r in range(N):
    for c in range(M):
        cnt = 0
        if dfs(r, c) and ans < cnt:
            ans = cnt
print(ans)