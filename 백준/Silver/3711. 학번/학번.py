N = int(input())
for _ in range(N):
    G = int(input())
    l = [0] * G
    for i in range(G):
        l[i] = int(input())
    m = 1
    while 1:
        flag = 1
        s = set()
        for i in l:
            r = i % m
            if r in s:
                flag = 0
                break
            else:
                s.add(r)
        if flag:
            break
        m += 1
    print(m)