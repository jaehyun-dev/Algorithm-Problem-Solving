import collections
A, B = map(int, input().split())
d = collections.deque()
d.append((A, 0))
flag = 1
ans = 0
while len(d) != 0:
    n, c = d.popleft()
    if B < n:
        continue
    d.append((n * 10 + 1, c + 1))
    d.append((n * 2, c + 1))
    if n == B:
        ans = c + 1
        flag = 0
        break
print(-1 if flag else ans)