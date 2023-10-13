import sys, heapq, math
input = sys.stdin.readline
INF = int(10e9)

def cal_dist(a, b):
    return math.sqrt(pow(abs(a[0] - b[0]), 2) + pow(abs(a[1] - b[1]), 2))

def dijik(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        edge = heapq.heappop(q)
        c = edge[0]
        n = edge[1]
        if dist[n] < c:
            continue
        for edge in graph[n]:
            cost = c + edge[0]
            if cost < dist[edge[1]]:
                dist[edge[1]] = cost
                heapq.heappush(q, (cost, edge[1]))

N, W = map(int, input().split())
M = float(input())

pos = [0]
for _ in range(N):
    pos.append(list(map(int, input().split())))

graph = [[] for _ in range(N + 1)]
dist = [INF] * (N + 1)
for _ in range(W):
    a, b = map(int, input().split())
    graph[a].append((0, b))
    graph[b].append((0, a))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if (0, j) not in graph[i]:
            graph[i].append((cal_dist(pos[i], pos[j]), j))

dijik(1)
print(int(dist[N] * 1000))