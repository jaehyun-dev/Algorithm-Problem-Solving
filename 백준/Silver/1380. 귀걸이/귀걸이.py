i = 0
while True:
    n = int(input())
    if n == 0:
        break
    s = []
    c = {}
    for j in range(n):
        c[str(j + 1)] = 0
        s.append(input().strip())
    for _ in range(2 * n - 1):
        p = list(input().split())
        c[p[0]] += 1
    res = ""
    for k in c:
        if c[k] == 1:
            res = s[int(k) - 1]
            break
    i += 1
    print(i, res)