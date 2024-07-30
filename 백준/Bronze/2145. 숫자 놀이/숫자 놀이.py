while 1:
    N = int(input())
    if not N:
        break
    while 9 < N:
        q, r = divmod(N, 10)
        N = q + r
    print(N)