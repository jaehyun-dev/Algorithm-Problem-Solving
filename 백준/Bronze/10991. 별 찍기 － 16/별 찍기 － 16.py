N = int(input())
for i in range(N):
    print(" " * (N - 1 - i), end="")
    print("*", end="")
    for _ in range(i):
        print(" *", end="")
    print()