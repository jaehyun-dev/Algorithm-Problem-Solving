import sys
input = sys.stdin.readline

dr = [[0, 0, 0], [1, 2, 3], [0, 1, 1], [1, 2, 2], [0, 0, -1], [0, 1, 2], [-1, -1, -1], [0, -1, -2], [1, 1, 1], [0, 1, 2], [0, 0, 1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [0, 1, 1], [0, 0, 1], [1, 1, 2], [0, -1, 0], [-1, 0, 1]]
dc = [[1, 2, 3], [0, 0, 0], [1, 0, 1], [0, 0, 1], [1, 2, 2], [1, 1, 1], [0, 1, 2], [1, 1, 1], [0, 1, 2], [1, 0, 0], [1, 2, 2], [0, 1, 1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [1, 2, 1], [0, 1, 0], [1, 1, 2], [1, 1, 1]]
l = len(dr)

def dfs(r, c):
    max_cnt = 0
    type = 0
    for i in range(l):
        cnt = graph[r][c]
        for j in range(3):
            nr = r + dr[i][j]
            nc = c + dc[i][j]
            if not M > nc >= 0 <= nr < N:
                cnt = 0
                break
            else:
                cnt += graph[nr][nc]
        max_cnt = max(cnt, max_cnt)
    return max_cnt

N, M = map(int, input().split())
graph = []
for n in range(N):
    graph.append(list(map(int, input().split())))
ans = 0
for r in range(N):
    for c in range(M):
        ans = max(ans, dfs(r, c))
print(ans)