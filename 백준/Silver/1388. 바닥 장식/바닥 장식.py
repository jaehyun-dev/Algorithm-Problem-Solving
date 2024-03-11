import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c):
    cur = graph[r][c]
    if vis[r][c] or prev != cur:
        return False
    vis[r][c] = 1
    if cur == '-':
        if c < M - 1:
            dfs(r, c + 1)
    elif cur == '|':
        if r < N - 1:
            dfs(r + 1, c)
    return True

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))
vis = [([0] * M) for _ in range(N)]
cnt = 0
for r in range(N):
    for c in range(M):
        prev = graph[r][c]
        if dfs(r, c):
            cnt += 1
print(cnt)