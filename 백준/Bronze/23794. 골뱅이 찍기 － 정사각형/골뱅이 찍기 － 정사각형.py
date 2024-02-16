N = int(input())
r = '@' * (N + 2)
c = '@' + " " * N + '@'
for i in range(N + 2):
    print(r if i == 0 or i == N + 1 else c)