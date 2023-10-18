import sys
input = sys.stdin.readline

def diffuse(r, c):
    a_0 = graph[r][c][0]
    if a_0 != -1:
        out = 0
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and graph[nr][nc][0] != -1:
                graph[nr][nc][1] += a_0 // 5
                out += 1
        graph[r][c][0] -= (a_0 // 5) * out

def purify():
    r = 0
    for c in range(C - 1):
        graph[r][c][1] = graph[r][c + 1][0]
    c = 0
    for r in range(1, puri[0]):
        graph[r][c][1] = graph[r - 1][c][0]
    r = puri[0]
    for c in range(1, C):
        graph[r][c][1] = graph[r][c - 1][0]
    c = C - 1
    for r in range(puri[0]):
        graph[r][c][1] = graph[r + 1][c][0]

    r = R - 1
    for c in range(C - 1):
        graph[r][c][1] = graph[r][c + 1][0]
    c = C - 1
    for r in range(puri[1] + 1, R):
        graph[r][c][1] = graph[r - 1][c][0]
    r = puri[1]
    for c in range(1, C):
        graph[r][c][1] = graph[r][c - 1][0]
    c = 0
    for r in range(puri[1] + 1, R - 1):
        graph[r][c][1] = graph[r + 1][c][0]

    for r in range(R):
        for c in range(C):
            if r == 0 or r == R - 1 or r == puri[0] or r == puri[1] or c == 0 or c == C - 1:
                graph[r][c][0] = graph[r][c][1]
                graph[r][c][1] = 0
    graph[puri[0]][1] = [0, 0]
    graph[puri[1]][1] = [0, 0]
    graph[puri[0]][0][0] = -1
    graph[puri[1]][0][0] = -1

R, C, T = map(int, input().split())
graph = []
puri = []
for i in range(R):
    graph.append(list(map(int, input().split())))
    if graph[i][0] == -1:
        puri.append(i)
for r in range(R):
    for c in range(C):
        graph[r][c] = [graph[r][c], 0]
for _ in range(T):
    for r in range(R):
        for c in range(C):
            diffuse(r, c)
    for r in range(R):
        for c in range(C):
            if graph[r][c][0] != -1:
                graph[r][c][0] += graph[r][c][1]
                graph[r][c][1] = 0
    purify()

ans = 0
for r in range(R):
    for c in range(C):
        ans += graph[r][c][0]
print(ans + 2)