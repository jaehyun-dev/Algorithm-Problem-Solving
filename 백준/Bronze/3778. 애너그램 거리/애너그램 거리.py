import sys
input = sys.stdin.readline
N = int(input())
for n in range(N):
    A = input().strip()
    B = input().strip()
    da = {}
    db = {}
    for i in A:
        if i in da:
            da[i] += 1
        else:
            da[i] = 1
    for i in B:
        if i in db:
            db[i] += 1
        else:
            db[i] = 1
    d = 0
    for i in da:
        if i in db:
            d += abs(da[i] - db[i])
        else:
            d += da[i]
    for i in db:
        if i not in da:
            d += db[i]
    print(f"Case #{n + 1}: {d}")