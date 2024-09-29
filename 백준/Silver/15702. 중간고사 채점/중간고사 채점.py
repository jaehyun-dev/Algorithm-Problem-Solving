N, M = map(int, input().split())
s = list(map(int, input().split()))
w = h = -1
for _ in range(M):
    l = list(input().split())
    n = int(l[0])
    r = l[1:]
    t = 0
    for i in range(N):
        if r[i] == 'O':
            t += s[i]
    if h < t:
        h = t
        w = n
    elif h == t and n < w:
        w = n
print(w, h)