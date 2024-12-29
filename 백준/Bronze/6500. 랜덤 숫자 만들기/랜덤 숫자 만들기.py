while 1:
    a0 = input()
    if a0 == '0':
        break
    s = set()
    s.add(a0)
    p = str(int(a0) ** 2)
    while 1:
        while len(p) < 8:
            p = '0' + p
        ai = p[2:6]
        if ai in s:
            break
        else:
            s.add(ai)
            p = str(int(ai) ** 2)
    print(len(s))