from itertools import combinations_with_replacement as combwr
n, m = map(int, input().split())
arr = list(map(str, sorted(list(map(int, input().split())))))
for i in combwr(arr, m):
    print(" ".join(i))