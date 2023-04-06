import collections
N, M = map(int, input().split())
A = list(map(int, input().split()))
dq = collections.deque()
for i in range(1, N + 1):
    dq.append(i)
count = 0
while A:
    num = A.pop(0)
    if dq.index(num) <= len(dq) - dq.index(num):
        while dq[0] != num:
            dq.append(dq.popleft())
            count += 1
    else:
        while dq[0] != num:
            dq.appendleft(dq.pop())
            count += 1
    dq.popleft()
print(count)