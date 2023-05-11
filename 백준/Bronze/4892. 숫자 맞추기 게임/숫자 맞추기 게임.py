count = 1
while 1:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = 3 * n0
    flag = (n1 % 2 == 0)
    if flag:
        n2 = n1 // 2
    else:
        n2 = (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    print(f"{count}.", "even" if flag else "odd", f"{n4}")
    count += 1