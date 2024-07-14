import collections

class p():
    def __init__(self, i):
        self.num = i
        self.cnt = 0

N, M, L = map(int, input().split())
d = collections.deque()
for i in range(1, N + 1):
    d.append(p(i))
d[0].cnt = 1
cnt = 0
while d:
    if d[0].cnt == M:
        break
    if d[0].cnt % 2:
        for _ in range(L):
            d.append(d.popleft())
        d[0].cnt += 1
    else:
        for _ in range(L):
            d.appendleft(d.pop())
        d[0].cnt += 1
    cnt += 1
print(cnt)