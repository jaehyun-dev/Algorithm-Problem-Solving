while 1:
    W = int(input())
    if not W:
        break
    s = []
    for _ in range(W):
        s.append(input())
    H = int(input())
    for _ in range(H):
        s.append(input())
    s.sort(key=lambda x: (['S', 'M', 'L'].index(x[0]), x[1]))
    print(*s)