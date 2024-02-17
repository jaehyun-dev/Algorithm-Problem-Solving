N = int(input())
r = '@' * 5 * N
c = '@' * N
for i in range(5):
    for _ in range(N):
        print(r if i == 0 else c)