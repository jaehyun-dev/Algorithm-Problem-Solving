graph = []
for _ in range(8):
    graph.append(input())
cnt = 0
for i in range(8):
    for j in range(8):
        if i % 2 == j % 2:
            if graph[i][j] == 'F':
                cnt += 1
print(cnt)