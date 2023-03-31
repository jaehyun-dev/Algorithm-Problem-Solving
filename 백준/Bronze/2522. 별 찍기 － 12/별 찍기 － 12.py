N = int(input())
for i in range(1, 2 * N):
    print(" " * abs(N - i) + "*" * (N - abs(N - i)))