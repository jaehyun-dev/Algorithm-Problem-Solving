T = int(input())
for _ in range(T):
    n = int(input())
    l = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if l[j]:
                l[j] = 0
            else:
                l[j] = 1
    print(sum(l))