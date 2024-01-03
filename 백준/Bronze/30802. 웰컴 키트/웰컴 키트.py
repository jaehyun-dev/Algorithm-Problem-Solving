import math
N = int(input())
a = list(map(int, input().split()))
T, P = map(int, input().split())
print(sum(list(map(lambda x: math.ceil(x / T), a))))
print(N // P, N - (N // P) * P)