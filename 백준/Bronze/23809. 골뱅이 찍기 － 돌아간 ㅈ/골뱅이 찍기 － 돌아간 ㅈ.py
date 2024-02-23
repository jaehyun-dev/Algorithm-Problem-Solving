N = int(input())
c = "@" * N
for i in range(5):
    for _ in range(N):
        print(c, end="")
        print(" " * N * (abs(2 - i) + 1) if i != 2 else c, end="")
        print(c)