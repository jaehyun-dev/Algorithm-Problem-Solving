N, T = map(int, input().split())
a = list(range(1, 2 * N)) + list(range(2 * N, 1, -1))
print(a[(T - 1) % (4 * N - 2)])