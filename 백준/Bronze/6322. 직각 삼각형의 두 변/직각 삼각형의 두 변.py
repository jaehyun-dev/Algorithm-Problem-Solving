i = 1
while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    flag = False
    if i != 1:
        print()
    print(f"Triangle #{i}")
    if a == -1:
        if c > b:
            print(f"a = {format(round((c ** 2 - b ** 2) ** (1 / 2), 4), '.3f')}")
        else:
            flag = True
    elif b == -1:
        if c > a:
            print(f"b = {format(round((c ** 2 - a ** 2) ** (1 / 2), 4), '.3f')}")

        else:
            flag = True
    else:
        print(f"c = {format(round((a ** 2 + b ** 2) ** (1 / 2), 4), '.3f')}")
    if flag:
        print("Impossible.")
    i += 1