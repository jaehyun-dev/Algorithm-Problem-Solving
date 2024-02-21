N = int(input())
c = '@' * N
r = c * 5
s = c + ' ' * N * 3 + c
for i in range(5):
    for _ in range(N):
        print(r if i == 0 or i == 4 else s)