import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    k = int(input())
    visited = [False] * k
    for i in range(k):
        a = list(input().split())
        o = a[0]
        n = int(a[1])
        if o == "I":
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, (-int(n), i))
            visited[i] = True
        else:
            if n == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])