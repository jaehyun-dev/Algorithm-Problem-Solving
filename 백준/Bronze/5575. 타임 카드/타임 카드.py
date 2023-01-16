for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    s = s2 - s1
    if s < 0:
        s += 60
        m2 -= 1
    m = m2 - m1
    if m < 0:
        m += 60
        h2 -= 1
    h = h2 - h1
    print(h, m, s)