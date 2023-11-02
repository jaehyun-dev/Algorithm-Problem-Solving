import sys, itertools
input = sys.stdin.readline
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
cnt = 0
row = [0] * N
col = [0] * N
for r in range(N):
    for c in range(N):
        cnt += graph[r][c]
        row[r] += graph[r][c]
        col[c] += graph[r][c]

ans = cnt
for case in itertools.combinations(list(range(N)), N // 2):
    power = 0
    other = cnt
    for i in case:
        other -= row[i] + col[i]
    for pair in itertools.combinations(case, 2):
        r, c = pair
        power += graph[r][c] + graph[c][r]
    other += power
    if abs(power - other) < ans:
        ans = abs(power - other)

print(ans)