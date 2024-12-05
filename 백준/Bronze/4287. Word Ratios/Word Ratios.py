while 1:
    l = input()
    if l == '#':
        break
    a, b, c = l.split()
    print(a, b, c, end=" ")
    for i in range(len(a)):
        d = ((ord(c[i]) - (ord(a[i]) - ord(b[i])) % 26) - 97) % 26 + 97
        print(chr(d), end="")
    print()