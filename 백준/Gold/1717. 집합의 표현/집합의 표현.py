import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def find(x):
    if x == p[x]:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def union(x, y):
    rep_x = find(x)
    rep_y = find(y)
    if rep_x < rep_y:
        p[rep_y] = rep_x
    else:
        p[rep_x] = rep_y

n, m = map(int, input().split())
p = list(range(n + 1))
for _ in range(m):
    o, a, b = map(int, input().split())
    if o:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)