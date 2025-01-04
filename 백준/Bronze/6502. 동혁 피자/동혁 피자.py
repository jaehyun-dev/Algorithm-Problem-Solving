i = 1
while 1:
    l = list(map(int, input().split()))
    if l == [0]:
        break
    r, w, l = l[0], l[1], l[2]
    if (w ** 2 + l ** 2) ** (1 / 2) <= 2 * r:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")
    i += 1