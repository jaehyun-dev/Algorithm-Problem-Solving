N = int(input())
graph = []
for _ in range(N):
    graph.append(input())
h = v = 0
for row in graph:
    cnt = 0
    for i in range(N):
        if row[i] == '.':
            cnt += 1
        else:
            if 1 < cnt:
                h += 1
            cnt = 0
    if 1 < cnt:
        h += 1
for i in range(N):
    cnt = 0
    for j in range(N):
        if graph[j][i] == '.':
            cnt += 1
        else:
            if 1 < cnt:
                v += 1
            cnt = 0
    if 1 < cnt:
        v += 1
print(h, v)