import itertools
T = int(input())
o = ["+", "-", " "]
for _ in range(T):
    N = int(input())
    a = [*(range(1, N + 1))]
    r = []
    for c in itertools.product(o, repeat=(N-1)):
        s = ""
        for i in range(N - 1):
            s += str(a[i])
            s += c[i]
        s += str(a[-1])
        if eval(s.replace(" ", "")) == 0:
            r.append(s)
    r.sort()
    for j in r:
        print(j)
    print()