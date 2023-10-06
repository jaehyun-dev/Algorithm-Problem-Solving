import sys
input = sys.stdin.readline

def recur(r, c):
    global ans, cnt
    visited[ord(graph[r][c]) - ord('A')] = True
    cnt += 1
    ans = max(ans, cnt)

    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < R and 0 <= nc < C and not visited[ord(graph[nr][nc]) - ord('A')]:
            recur(nr, nc)

    visited[ord(graph[r][c]) - ord('A')] = False
    cnt -= 1

R, C = map(int, input().split())
graph = []
visited = [False] * 26

for _ in range(R):
    graph.append(input().strip())

ans = 0
cnt = 0
recur(0, 0)
print(ans)