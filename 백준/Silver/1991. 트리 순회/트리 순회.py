class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_ord(node):
    print(node.data, end = "")
    if node.left != None:
        pre_ord(node.left)
    if node.right != None:
        pre_ord(node.right)

def in_ord(node):
    if node.left != None:
        in_ord(node.left)
    print(node.data, end = "")
    if node.right != None:
        in_ord(node.right)

def post_ord(node):
    if node.left != None:
        post_ord(node.left)
    if node.right != None:
        post_ord(node.right)
    print(node.data, end = "")

N = int(input())
tree = []
for _ in range(N):
    l = input().split()
    flag = True
    for i in tree:
        if i.data == l[0]:
            node = i
            flag = False
            break
    if flag:
        node = Node(l[0])
        tree.append(node)
    if l[1] != '.':
        flag = True
        for i in tree:
            if i.data == l[1]:
                left = i
                flag = False
                break
        if flag:
            left = Node(l[1])
            tree.append(left)
        node.left = left
    if l[2] != '.':
        flag = True
        for i in tree:
            if i.data == l[2]:
                right = i
                flag = False
                break
        if flag:
            right = Node(l[2])
            tree.append(right)
        node.right = right

pre_ord(tree[0])
print()
in_ord(tree[0])
print()
post_ord(tree[0])