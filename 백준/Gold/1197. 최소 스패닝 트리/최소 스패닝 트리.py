import sys
input = sys.stdin.readline

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)
    s = min(rep_x, rep_y)
    l = max(rep_x, rep_y)
    if rep_x == rep_y:
        pass
    else:
        p[l] = s

N, E = map(int, input().split())
p = list(range(N + 1))
edge = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))
edge.sort()

i = 0
cnt = 0
ans = 0
while cnt < N - 1:
    C, A, B = edge[i]
    a = find(A)
    b = find(B)
    if find(A) != find(B):
        union(a, b)
        cnt += 1
        ans += C
    i += 1
print(ans)