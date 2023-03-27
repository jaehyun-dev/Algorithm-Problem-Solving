import sys
sys.setrecursionlimit(10**9) # set recursion limit to avoid recursion depth error
input = sys.stdin.readline

def dfs(node, parent):
    for child in graph[node]:
        if child != parent:
            parents[child] = node
            dfs(child, node)

n = int(input())
graph = [[] for _ in range(n+1)]
parents = [0] * (n+1)

# build the graph
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)

for i in range(2, n+1):
    print(parents[i])