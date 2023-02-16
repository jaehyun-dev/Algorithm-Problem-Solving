from collections import deque

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacent_node = []
        self.visited = False

    def add_connection(self, name):
        self.adjacent_node.append(name)
        name.adjacent_node.append(self)

N, M, V = map(int, input().split())

nodes = {}
edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))

for i in range(1, N + 1):
    node_name = i
    current_node = Node(i)
    nodes[i] = current_node

for edge in edges:
    if edge[1] not in nodes[edge[0]].adjacent_node:
        nodes[edge[0]].add_connection(nodes[edge[1]])

def dfs(graph, start_node):
    stack = deque()
    ans = []

    for node in graph.values():
        node.visited = 0

    for i in range(1, N + 1):
        nodes[i].adjacent_node.sort(reverse=True, key=lambda x: x.name)

    start_node.visited = 1
    stack.append(start_node)

    while stack:
        current_node = stack.pop()
        current_node.visited = 2
        ans.append(current_node.name)
        for neighbor in sorted(current_node.adjacent_node, reverse=True, key=lambda x: x.name):
            if neighbor.visited != 2:
                neighbor.visited = 1
                if neighbor in stack:
                    stack.remove(neighbor)
                stack.append(neighbor)

    return ans


def bfs(graph, start_node):
    queue = deque()
    ans = []

    for node in graph.values():
        node.visited = False

    for i in range(1, N + 1):
        nodes[i].adjacent_node.sort(key=lambda x: x.name)

    start_node.visited = True
    queue.append(start_node)

    while queue:
        current_node = queue.popleft()
        ans.append(current_node.name)
        for neighbor in current_node.adjacent_node:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)

    return ans

for node in dfs(nodes, nodes[V]):
    print(node, end=" ")

print()

for node in bfs(nodes, nodes[V]):
    print(node, end=" ")