E, S, M = map(int, input().split())
i = 1
a = b = c = 1
while 1:
    if ([*range(15)][(a - 1) % 15] + 1, [*range(28)][(b - 1) % 28] + 1, [*range(19)][(c - 1) % 19] + 1) == (E, S, M):
        print(i)
        break
    else:
        a += 1
        b += 1
        c += 1
        i += 1