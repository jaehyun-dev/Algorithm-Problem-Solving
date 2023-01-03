import math
n_1, n_2, n_12 = map(int, input().split())
print(math.floor(((n_1 + 1) * (n_2 + 1)) / (n_12 + 1) - 1))