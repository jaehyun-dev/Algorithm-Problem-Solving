import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs1(r, c):
    if visited1[r][c]:
        return False
    else:
        visited1[r][c] = True
    clr = graph[r][c]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited1[nr][nc] and graph[nr][nc] == clr:
            dfs1(nr, nc)
    return True

def dfs2(r, c):
    if visited2[r][c]:
        return False
    else:
        visited2[r][c] = True
    clr = graph[r][c]
    flag = False
    if clr == 'R' or clr == 'G':
        flag = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc]:
            if flag:
                if graph[nr][nc] == 'R' or graph[nr][nc] == 'G':
                    dfs2(nr, nc)
            else:
                if graph[nr][nc] == clr:
                    dfs2(nr, nc)
    return True

N = int(input())
graph = []
visited1 = []
visited2 = []
cnt1 = 0
cnt2 = 0
for _ in range(N):
    graph.append(list(input().strip()))
    temp = list([False] * N)
    visited1.append(temp)
    temp = list([False] * N)
    visited2.append(temp)
for r in range(N):
    for c in range(N):
        if dfs1(r, c):
            cnt1 += 1
        if dfs2(r, c):
            cnt2 += 1
print(cnt1, cnt2)