N = int(input())
c = '@' * N
a = c + ' ' * N * 3 + c
b = c * 5
for i in range(5):
    for _ in range(N):
        print(b if i == 2 or i == 4 else a)