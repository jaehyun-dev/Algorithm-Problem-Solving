import sys, heapq
input = sys.stdin.readline
INF = int(10e9)

def dijik(start):
    q = []
    q.append((0, start))
    dist[start] = 0
    while q:
        edge = heapq.heappop(q)
        cost = edge[0]
        node = edge[1]
        if dist[node] < cost:
            continue
        for e in graph[node]:
            if cost + e[0] < dist[e[1]]:
                dist[e[1]] = cost + e[0]
                heapq.heappush(q, (dist[e[1]], e[1]))

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
dist = [INF] * (V + 1)
K = int(input())
for _ in range(E):
    u, v, w = map(int, input().split())
    flag = True
    if graph[u]:
        for i in range(len(graph[u])):
            if graph[u][i][1] == v:
                if w < graph[u][i][0]:
                    graph[u][i] = (w, v)
                flag = False
                break
    if flag:
        graph[u].append((w, v))

dijik(K)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])