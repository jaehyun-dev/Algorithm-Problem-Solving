from collections import deque
n, m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            y = i
            x = j
            break

def bfs(y, x):
    ans = [[0] * m for _ in range(n)]
    ans[y][x] = 0
    visited = [[False] * m for _ in range(n)]
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)

    visited[y][x] = True
    que = deque()
    que.append((y, x))

    while que:
        y, x = que.popleft()
        dist = ans[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < n and 0 <= nx < m):
                continue
            if arr[ny][nx] == 0:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                ans[ny][nx] = dist + 1
                que.append((ny, nx))

    return [ans, visited]

a = bfs(y, x)
ans = a[0]
visited = a[1]

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and arr[i][j] == 1:
            ans[i][j] = -1

for i in ans:
    print(*i)