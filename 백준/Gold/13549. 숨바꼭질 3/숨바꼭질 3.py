import sys, collections
input = sys.stdin.readline
MAX = int(1e5 + 1)

N, K = map(int, input().split())
q = collections.deque()
vis = [-1] * MAX
q.append(N)
vis[N] = 0

while q:
    n = q.popleft()
    if n == K:
        print(vis[n])
        break
    if 0 <= n - 1 < MAX and vis[n - 1] == -1:
        vis[n - 1] = vis[n] + 1
        q.append(n - 1)
    if 0 <= 2 * n < MAX and vis[2 * n] == -1:
        vis[2 * n] = vis[n]
        q.appendleft(2 * n)
    if 0 <= n + 1 < MAX and vis[n + 1] == -1:
        vis[n + 1] = vis[n] + 1
        q.append(n + 1)