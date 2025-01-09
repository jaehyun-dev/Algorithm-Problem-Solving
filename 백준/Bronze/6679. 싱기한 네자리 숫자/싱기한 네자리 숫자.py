def to_base(n, base):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

digits = "0123456789ABCDEF"
for i in range(1000, 10000):
    dc = str(i)
    p = 0
    for j in dc:
        p += int(j)
    dz = to_base(i, 12)
    c = 0
    for j in dz:
        if j.isdigit():
            c += int(j)
        else:
            c += digits.index(j)
    if p != c:
        continue
    p = c
    hx = to_base(i, 16)
    c = 0
    for j in hx:
        if j.isdigit():
            c += int(j)
        else:
            c += digits.index(j)
    if p == c:
        print(i)