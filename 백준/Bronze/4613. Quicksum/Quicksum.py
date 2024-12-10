while 1:
    l = input()
    if l == '#':
        break
    s = 0
    for i in range(len(l)):
        c = l[i]
        if c == ' ':
            continue
        else:
            s += (ord(c) - 64) * (i + 1)
    print(s)