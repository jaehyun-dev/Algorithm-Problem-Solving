import math
r = [3, 6, 9, 12, 15]
s = [100, 80, 60, 40, 20]
T = int(input())
for _ in range(T):
    f = list(map(float, input().split()))
    x = f[::2]
    y = f[1::2]
    N = M = 0
    for i in range(3):
        dn = math.sqrt(x[i] ** 2 + y[i] ** 2)
        dm = math.sqrt(x[i + 3] ** 2 + y[i + 3] ** 2)
        fn = 1
        fm = 1
        for j in range(5):
            if (not fn) and (not fm):
                break
            if dn <= r[j] and fn:
                N += s[j]
                fn = 0
            if dm <= r[j] and fm:
                M += s[j]
                fm = 0
    if N == M:
        ans = "TIE"
    elif N < M:
        ans = "PLAYER 2 WINS"
    else:
        ans = "PLAYER 1 WINS"
    print(f"SCORE: {N} to {M}, {ans}.")