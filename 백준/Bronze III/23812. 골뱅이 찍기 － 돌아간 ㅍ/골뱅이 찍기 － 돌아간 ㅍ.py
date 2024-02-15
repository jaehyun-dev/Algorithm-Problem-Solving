N = int(input())
r = '@' * N + '   ' * N + '@' * N
c = '@' * 5 * N
i = 0
while i < 5:
    for _ in range(N):
        print(r if i % 2 == 0 else c)
    i += 1