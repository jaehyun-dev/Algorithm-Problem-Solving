class node():
    def __init__(self, i):
        self.idx = i
        self.parent = 0
        self.children = []

def dfs(node):
    global cnt
    if not len(node.children):
        cnt += 1
    for n in node.children:
        dfs(n)

N = int(input())
a = list(map(int, input().split()))
nodes = []
roots = []
for i in range(N):
    nodes.append(node(i))
for i in range(N):
    if a[i] == -1:
        roots.append(nodes[i])
        continue
    nodes[i].parent = nodes[a[i]]
    nodes[a[i]].children.append(nodes[i])
cnt = 0
t = int(input())
if nodes[t].parent != 0:
    nodes[t].parent.children.remove(nodes[t])
else:
    for root in roots:
        if root.idx == t:
            roots.remove(root)
            break
for node in roots:
    dfs(node)
print(cnt)