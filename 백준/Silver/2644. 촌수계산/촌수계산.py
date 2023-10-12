import sys, collections
input = sys.stdin.readline
n = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
vis = [0] * (n + 1)

a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

q = collections.deque()
q.append(a)
vis[a] = 1
while q:
    x = q.popleft()
    for i in range(1, n + 1):
        if graph[x][i] == 1 and not vis[i]:
            graph[a][i] = graph[a][x] + 1
            vis[i] = 1
            q.append(i)
ans = graph[a][b]
print(ans if ans else -1)