while 1:
    n = int(input())
    if n == -1:
        break
    a = []
    b = []
    i = 1
    while i < n // 2 + 1:
        if n % i == 0 and i not in b:
            a.append(i)
            q = n // i
            if i != q:
                b.append(q)
        i += 1
    d = a + b[::-1][:-1]
    if sum(d) == n:
        print(str(n) + " = ", end="")
        print(*d, sep=" + ")
    else:
        print(f"{n} is NOT perfect.")