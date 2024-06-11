flag = 0
graph = []
for _ in range(10):
    a = list(input().split())
    if len(set(a)) == 1:
        flag = 1
        break
    graph.append(a)
if not flag:
    for j in range(10):
        flag = 1
        prev = graph[0][j]
        for i in range(1, 10):
            if graph[i][j] != prev:
                flag = 0
                break
            prev = graph[i][j]
        if flag:
            break
print(flag)