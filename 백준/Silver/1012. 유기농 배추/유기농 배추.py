import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                count += 1
    print(count)