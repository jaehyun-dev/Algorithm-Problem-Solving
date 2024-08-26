import queue
q = queue.PriorityQueue()
cnt = 0
N = int(input())
d = int(input())
for _ in range(N - 1):
    a = int(input())
    q.put((-a, a))
while not q.empty():
    a = q.get()[1]
    if a < d:
        break
    d += 1
    a -= 1
    q.put((-a, a))
    cnt += 1
print(cnt)