T = int(input())
for _ in range(T):
    N = int(input())
    m = 0
    p = 100000
    for _ in range(N):
        W, C = map(int, input().split())
        if m < W / C:
            m = W / C
            p = C
        elif m == W / C:
            if C < p:
                p = C
    print(p)