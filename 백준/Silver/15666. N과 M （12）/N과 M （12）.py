from itertools import combinations_with_replacement as cwr
from collections import Counter
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
c = Counter(cwr(arr, m))
for i in c:
    for j in range(m):
        print(i[j], end=" ")
    print()