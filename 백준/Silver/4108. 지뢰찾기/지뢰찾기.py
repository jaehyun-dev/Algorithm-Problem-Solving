while 1:
    R, C = map(int, input().split())
    if not R * C:
        break
    graph = []
    for _ in range(R):
        graph.append(input())
    ans = []
    for r in range(R):
        temp = ""
        for c in range(C):
            if graph[r][c] == ".":
                cnt = 0
                for (dr, dc) in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
                     nr = r + dr
                     nc = c + dc
                     if 0 <= nr < R and 0 <= nc < C:
                        if graph[nr][nc] == "*":
                            cnt += 1
                temp += str(cnt)
            else:
                temp += "*"
        ans.append(temp)
    for row in ans:
        print(row)