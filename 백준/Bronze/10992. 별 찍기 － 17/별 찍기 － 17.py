N = int(input())
for i in range(N):
    if i == 0:
        print(" " * (N - 1), end="")
        print("*")
    elif i == (N - 1):
        print("*" * (2 * N - 1))
    else:
        print(" " * (N - 1 - i), end="")
        print("*", end="")
        print(" " * (2 * i - 1), end="")
        print("*")