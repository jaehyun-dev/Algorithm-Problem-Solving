import collections
import sys
input = sys.stdin.readline
dq = collections.deque()
N = int(input())
for _ in range(N):
    l = list(map(int, input().split()))
    c = l[0]
    if c == 1:
        dq.appendleft(l[1])
    elif c == 2:
        dq.append(l[1])
    elif c == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif c == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif c == 5:
        print(len(dq))
    elif c == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif c == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)