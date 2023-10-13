import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

def dijik(start):
    dist = [INF] * (N + 1)
    pq = []
    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        t, node = heapq.heappop(pq)
        if dist[node] < t:
            continue
        for edge in graph[node]:
            time = t + edge[0]
            if time < dist[edge[1]]:
                dist[edge[1]] = time
                heapq.heappush(pq, (time, edge[1]))

    return dist

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))

ans = 0
for i in range(1, N + 1):
    go = dijik(i)[X]
    back = dijik(X)[i]
    if ans < go + back:
        ans = go + back

print(ans)