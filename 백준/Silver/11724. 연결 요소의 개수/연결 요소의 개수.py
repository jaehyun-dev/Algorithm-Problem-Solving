import sys
from collections import deque

class Node:
    def __init__(self, node):
        self.name = node
        self.adjacent_node = []
        self.visited = False

    def add_connection(self, node):
        self.adjacent_node.append(node)
        node.adjacent_node.append(self)

input = sys.stdin.readline
N, M = map(int, input().split())
nodes = [None]

for i in range(N):
        nodes.append(Node(i + 1))

for _ in range(M):
    u, v = map(int, input().split())
    nodes[u].add_connection(nodes[v])

count = 0
def dfs(node):
    global count
    stack = deque()

    if not node.visited:
        stack.append(node)
        while stack:
            current = stack.pop()
            current.visited = 2
            for node in current.adjacent_node:
                if not node.visited:
                    node.visited = 1
                    stack.append(node)
        count += 1


for node in nodes:
    if node is not None:
        dfs(node)

print(count)