N = int(input())
r = "@" * 5 * N
c = "@" * N
i = 0
while i < 5:
    if i == 0 or i == 2:
        for _ in range(N):
            print(r)
    else:
        for _ in range(N):
            print(c)
    i += 1