N = int(input())
for i in range(2 * N - 1):
    print("*" * (N - abs(N - i - 1)))