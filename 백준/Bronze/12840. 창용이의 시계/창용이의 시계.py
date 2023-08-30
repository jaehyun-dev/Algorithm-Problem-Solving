import sys
input = sys.stdin.readline
h, m, s = map(int, input().split())
t = h * 3600 + m * 60 + s
q = int(input())
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        t += a[1]
    elif a[0] == 2:
        t -= a[1]
    else:
        t_ = t % 86400
        h_ = t_ // 3600
        t_ %= 3600
        m_ = t_ // 60
        s_ = t_ % 60
        print(h_, m_, s_)