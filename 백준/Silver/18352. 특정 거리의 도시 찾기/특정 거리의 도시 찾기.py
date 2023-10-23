import sys, collections, heapq
input = sys.stdin.readline

def bfs(node):
    q = collections.deque()
    q.append((0,node))
    vis.add(node)
    while q:
        c, n = q.popleft()
        if c == K:
            break
        for a in graph[n]:
            if a not in vis:
                q.append((c + 1, a))
                vis.add(a)
                if c + 1 == K:
                    heapq.heappush(ans, a)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
ans = []
vis = set()
bfs(X)
if len(ans) == 0:
    print(-1)
while ans:
    print(heapq.heappop(ans))