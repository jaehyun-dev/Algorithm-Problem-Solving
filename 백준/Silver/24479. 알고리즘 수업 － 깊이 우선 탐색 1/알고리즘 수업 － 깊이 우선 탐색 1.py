import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

class Node():
    def __init__(self, num):
        self.num = num
        self.vis = False
        self.adj = []
        self.turn = 0

N, M, R = map(int, input().split())
nodes = [Node(0)]
for i in range(1, N + 1):
    nodes.append(Node(i))
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u].adj.append(v)
    nodes[v].adj.append(u)
for node in nodes:
    node.adj.sort()

def dfs(nodes, R):
    global i
    nodes[R].turn = i
    i += 1
    nodes[R].vis = True
    for num in nodes[R].adj:
        if (not nodes[num].vis):
            dfs(nodes, num)

i = 1
dfs(nodes, R)
for i in range(1, N + 1):
    print(nodes[i].turn)