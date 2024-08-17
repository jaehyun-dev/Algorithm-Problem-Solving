R, C = map(int, input().split())
graph = []
vis = [0] * R
for _ in range(R):
    graph.append(input())
rank = 1
ans = [0] * R
for c in range(C):
    flag = 0
    for r in range(R):
        if not vis[r]:
            if graph[r][C - 2 - c] != '.':
                ans[int(graph[r][C - 2 - c]) - 1] = rank
                vis[r] = 1
                flag = 1
    if flag:
        rank += 1
    if sum(vis) == 9:
        break
for i in ans:
    if i != 0:
        print(i)