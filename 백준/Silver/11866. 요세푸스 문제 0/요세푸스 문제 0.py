n, k = map(int, input().split())
arr = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

for i in range(1, n + 1):
    exec(f"node_{i} = Node({i})")

for i in range(1, n + 1):
    if i == n:
        exec(f"node_{i}.next = node_{1}")
    else:
        exec(f"node_{i}.next = node_{i + 1}")

head_node = Node(0)
head_node.next = node_1

for i in range(1, n + 1):
    if i == 1:
        exec(f"node_{i}.previous = node_{n}")
    else:
        exec(f"node_{i}.previous = node_{i - 1}")

def pop(node):
    node.previous.next, node.next.previous = node.next, node.previous
    return node.data

def search(node):
    for _ in range(k):
        node = node.next
    arr.append(node.data)
    return node

count = 0
node = head_node
while count < n:
    node = search(node)
    pop(node)
    count += 1

print("<", end="")
for i in range(n - 1):
    print(f"{arr[i]}, ", end="")
print(f"{arr[-1]}>")