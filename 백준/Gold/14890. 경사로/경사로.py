import sys
input = sys.stdin.readline

def check(arr):
    h = arr[0]
    cnt = 1
    flag = False
    i = 1
    while i < N:
        d = h - arr[i]
        if d == 1:
            if flag and cnt < L:
                return False
            cnt = 1
            flag = True
            if cnt == L:
                cnt = 0
                flag = False
        elif d == -1:
            if cnt < L:
                return False
            cnt = 1
            flag = False
        elif d == 0:
            cnt += 1
            if flag:
                if cnt == L:
                    cnt = 0
                    flag = False
        else:
            return False
        h = arr[i]
        i += 1
    if flag and cnt < L:
        return False
    return True

N, L = map(int, input().split())
graph = []
ans = 0
for _ in range(N):
    graph.append(list(map(int, input().split())))
tp = [([0] * N) for _ in range(N)]
for r in range(N):
    for c in range(N):
        tp[c][r] = graph[r][c]
for r in range(N):
    if check(graph[r]):
        ans += 1
    if check(tp[r]):
        ans += 1
print(ans)