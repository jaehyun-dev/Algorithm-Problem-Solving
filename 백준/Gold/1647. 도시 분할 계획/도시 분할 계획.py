import sys, heapq
input = sys.stdin.readline

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    x, y = min(x, y), max(x, y)
    if find(x) != find(y):
        p[find(y)] = find(x)

N, M = map(int, input().split())

def kruskal():
    cnt = 0
    global cost
    global edges
    while cnt < N - 1:
        C, A, B = heapq.heappop(edges)
        if find(A) != find(B):
            union(A, B)
            cost += C
            heapq.heappush(linked, C)
            cnt += 1

p = []
for i in range(N + 1):
    p.append(i)

edges = []
linked = []
cost = 0
for _ in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(edges, [C, A, B])

kruskal()
cost -= linked[-1]
print(cost)