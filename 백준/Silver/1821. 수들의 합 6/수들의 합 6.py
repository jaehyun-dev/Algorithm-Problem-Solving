import itertools

N, F = map(int, input().split())
for perm in itertools.permutations(list(range(1, N + 1))):
    a = perm
    while 1 < len(a):
        temp = []
        for i in range(len(a) - 1):
            temp.append(a[i] + a[i + 1])
        a = temp
    if a[0] == F:
        print(*perm)
        break