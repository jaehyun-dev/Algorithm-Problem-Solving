N = int(input())
c = '@' * N
t = c * 3 + ' ' * N + c
m = (c + ' ' * N) * 2 + c
b = c + ' ' * N + c * 3
for i in range(5):
    for _ in range(N):
        if i == 0:
            print(t)
        elif i == 4:
            print(b)
        else:
            print(m)