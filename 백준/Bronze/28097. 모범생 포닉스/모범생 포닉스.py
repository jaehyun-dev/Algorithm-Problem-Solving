N = int(input())
T = list(map(int, input().split()))
a = sum(T) + 8 * (N - 1)
print(a // 24, a % 24)