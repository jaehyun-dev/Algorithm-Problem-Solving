while 1:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break
    N = l[0]
    p = l[1]
    print(p, end=" ")
    for i in range(2, N + 1):
        c = l[i]
        if p != c:
            print(c, end=" ")
        p = c
    print("$")