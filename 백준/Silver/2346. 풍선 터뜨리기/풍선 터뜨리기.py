import collections
N = int(input())
l = list(map(int, input().split()))
dq = collections.deque()
for i in range(N):
    dq.append((i + 1, l[i]))
while dq:
    n, r = dq.popleft()
    print(n, end=" ")
    if 0 < r:
        dq.rotate(-r + 1)
    else:
        dq.rotate(-r)