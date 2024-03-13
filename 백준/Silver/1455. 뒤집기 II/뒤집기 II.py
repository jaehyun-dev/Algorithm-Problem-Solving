N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))
cnt = 0
flip = [([0] * M) for _ in range(N)]
for r in range(N)[::-1]:
    for c in range(M)[::-1]:
        if graph[r][c] ^ (flip[r][c] % 2):
            cnt += 1
            for i in range(r + 1):
                for j in range(c + 1):
                    flip[i][j] += 1
print(cnt)