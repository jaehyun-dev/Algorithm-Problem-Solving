from itertools import combinations_with_replacement as combwr
n, m = map(int, input().split())
arr = list(map(str, [*range(1, n + 1)]))
for i in combwr(arr, m):
    print(" ".join(i))