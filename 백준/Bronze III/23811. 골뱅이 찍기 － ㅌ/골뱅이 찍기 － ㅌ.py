N = int(input())
r = '@' * 5 * N
c = '@' * N
i = 0
while i < 5:
    for _ in range(N):
        print(r if i % 2 == 0 else c)
    i += 1