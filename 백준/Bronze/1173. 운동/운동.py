N, m, M, T, R = map(int, input().split())
s = 0
t = 0
p = m
while 1:
    if t == N:
        break
    if M < m + T:
        s = -1
        break
    if M < p + T:
        p = max(m, p - R)
    else:
        p += T
        t += 1
    s += 1
print(s)