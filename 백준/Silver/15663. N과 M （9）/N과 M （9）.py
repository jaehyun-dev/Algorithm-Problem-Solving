from itertools import permutations as p_
from collections import Counter
n, m = map(int, input().split())
arr = list(map(int, input().split()))
c = sorted(Counter(p_(arr, m)))
for i in c:
    for j in range(m):
        print(i[j], end=" ")
    print()