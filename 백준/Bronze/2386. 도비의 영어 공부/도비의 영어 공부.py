while 1:
    l = input()
    if l == '#':
        break
    c = l[0]
    s = l[2:]
    cnt = 0
    for i in s:
        if i in [c, chr(ord(c) - 32)]:
            cnt += 1
    print(c, cnt)