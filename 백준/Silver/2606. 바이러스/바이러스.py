from collections import deque

class Node:
    def __init__(self, num):
        self.name = num
        self.adjacent_nodes = []
        self.visited = False

    def add_connection(self, node):
        self.adjacent_nodes.append(node)
        node.adjacent_nodes.append(self)

def bfs(graph, start_node):
    queue = deque()

    for node in graph.values():
        node.visited = False

    start_node.visited = True
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        for neighbor in current_node.adjacent_nodes:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)

V = int(input())
E = int(input())
nodes = {}
for i in range(1, V + 1):
    nodes[i] = Node(i)
for _ in range(E):
    a, b = map(int, input().split())
    nodes[a].add_connection(nodes[b])

bfs(nodes, nodes[1])

count = 0
for i in range(1, V + 1):
    if nodes[i].visited:
        count += 1

print(count - 1)