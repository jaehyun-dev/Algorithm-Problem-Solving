n = int(input())

class Node:
    def __init__(self):
        self.data = 0

heap = [None]
heap_dic = {}
for i in range(1, n + 1):
    a = Node()
    heap.append(a)
    heap_dic[i] = a

heap[1].data = n
heap[n].data = 1

nodes_num = n - 1

while nodes_num > 1:
    string = bin(nodes_num)[2:]
    i = 2
    while i <= len(string):
        heap[int(string[:i], 2) // 2] = heap[int(string[:i], 2)]
        i += 1
    heap[1].data = nodes_num
    nodes_num -= 1

for i in range(1, n):
    print(heap_dic[i].data, end=" ")
print(1)