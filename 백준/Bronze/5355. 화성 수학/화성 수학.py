T = int(input())
for _ in range(T):
    l = input().split()
    n = float(l[0])
    for o in l[1:]:
        if o == "@":
            n *= 3
        elif o == "%":
            n += 5
        elif o == "#":
            n -= 7
    print(format(n, '.2f'))