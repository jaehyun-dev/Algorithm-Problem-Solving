while 1:
    l = input()
    if l == "#":
        break
    a = [0] * 26
    for c in l:
        i = ord(c)
        if 65 <= i < 91:
            a[i - 65] = 1
        elif 97 <= i < 123:
            a[i - 97] = 1
    print(sum(a))