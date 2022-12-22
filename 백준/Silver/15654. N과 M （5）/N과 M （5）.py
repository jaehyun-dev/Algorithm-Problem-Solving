from itertools import permutations
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr_str = []
for i in arr:
    arr_str.append(str(i))
for i in permutations(arr_str, m):
    print(" ".join(i))