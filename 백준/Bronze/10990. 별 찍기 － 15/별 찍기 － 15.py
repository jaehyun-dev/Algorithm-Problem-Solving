N = int(input())
for i in range(1, 1 + N):
    print(" " * (N - i), end="")
    print("*", end="")
    print(" " * (2 * (i - 1) - 1), end="")
    print("" if i == 1 else "*")