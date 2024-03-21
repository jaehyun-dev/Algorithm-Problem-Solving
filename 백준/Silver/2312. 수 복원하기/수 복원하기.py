T = int(input())
for _ in range(T):
    N = int(input())
    d = {}
    for i in range(N + 1):
        d[i] = 0
    num = 2
    while 1:
        if N == 1:
            break
        if N % num != 0:
            num += 1
        else:
            N /= num
            d[num] += 1
    for i in d:
        if d[i] != 0:
            print(i, d[i])