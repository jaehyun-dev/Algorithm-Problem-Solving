import collections

class Node:
    def __init__(self, value):
        self.value = value
        self.adj_list = set()
        self.cnt = 0
        self.visited = False

def bfs():
    queue = collections.deque()
    queue.append(node_list[1])
    ans = 100
    while queue:
        cur = queue.popleft()
        cur.visited = True
        for idx in cur.adj_list:
            adj_node = node_list[idx]
            if not adj_node.visited:
                adj_node.visited = True
                queue.append(adj_node)
                adj_node.cnt = cur.cnt + 1
                if adj_node.value == 100:
                    if adj_node.cnt < ans:
                        ans = adj_node.cnt
    return ans

N, M = map(int, input().split())
ladder = []
snake = []
for _ in range(N):
    ladder.append(tuple(map(int, input().split())))
for _ in range(M):
    snake.append(tuple(map(int, input().split())))
node_list = [None]
for i in range(100):
    node_list.append(Node(i + 1))
for i in range(len(ladder)):
    node_list[ladder[i][0]] = node_list[ladder[i][1]]
for i in range(len(snake)):
    node_list[snake[i][0]] = node_list[snake[i][1]]

for i in range(1, 101):
    for j in range(1, 7):
        if node_list[i].value + 7 - j <= 100:
            node_list[node_list[i].value].adj_list.add(node_list[i].value + 7 - j)

print(bfs())