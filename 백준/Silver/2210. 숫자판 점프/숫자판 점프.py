import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(r, c, i, num):
    num += graph[r][c]
    if i == 5:
        return num_set.add(num)
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            dfs(nr, nc, i + 1, num)

graph = []
num_set = set()
for _ in range(5):
    graph.append(list(input().split()))
for r in range(5):
    for c in range(5):
        dfs(r, c, 0, '')
print(len(num_set))