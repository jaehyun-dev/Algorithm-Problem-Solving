import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijik(start):
    q = []
    dist[start] = 0
    q.append((0, start))
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for e in graph[node]:
            if cost + e[0] < dist[e[1]]:
                dist[e[1]] = cost + e[0]
                heapq.heappush(q, (cost + e[0], e[1]))

N = int(input())
dist = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]
M = int(input())
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((C, B))
start, end = map(int, input().split())
dijik(start)
print(dist[end])