import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

def dijik(start):
    dist = [INF] * (N + 1)
    q = []
    q.append((0, start))
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for c, n in graph[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(q, (dist[n], n))
    return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().split())
dist0 = dijik(1)
dist1 = dijik(v1)
dist2 = dijik(v2)

ans = min(dist0[v1] + dist1[v2] + dist2[N], dist0[v2] + dist2[v1] + dist1[N])
print(-1 if ans >= INF else ans)