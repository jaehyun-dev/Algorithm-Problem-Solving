import collections
N, K = map(int, input().split())
def bfs():
    q = collections.deque()
    dis = [0] * (10 ** 5 + 1)
    q.append(N)
    while q:
        c = q.popleft()
        if c == K:
            print(dis[c])
            break
        else:
            for i in [c - 1, c + 1, c * 2]:
                if 0 <= i <= 10 ** 5 and not dis[i]:
                    dis[i] = dis[c] + 1
                    q.append(i)
bfs()