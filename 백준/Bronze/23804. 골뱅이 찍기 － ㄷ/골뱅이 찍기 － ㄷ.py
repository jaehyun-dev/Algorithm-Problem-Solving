N = int(input())
r = '@' * 5 * N
c = '@' * N
for i in range(5):
    for _ in range(N):
        print(r if i == 0 or i == 4 else c)