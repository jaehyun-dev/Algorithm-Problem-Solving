import sys

def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = left_child_index + 1

    largest = index

    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index

    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)

def reverse_heapify(tree, index):
    parent_index = index // 2

    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
        swap(tree, index, parent_index)
        reverse_heapify(tree, parent_index)

class PriorityQueue:
    def __init__(self):
        self.heap = [None]

    def insert(self, data):
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap) - 1)

    def extract_max(self):
        swap(self.heap, 1, len(self.heap) - 1)
        return_value = self.heap.pop()
        heapify(self.heap, 1, len(self.heap))
        return return_value

priority_queue = PriorityQueue()

input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    a = int(input())
    if a != 0:
        priority_queue.insert(a)
    else:
        if len(priority_queue.heap) == 1:
            print(0)
        else:
            print(priority_queue.extract_max())