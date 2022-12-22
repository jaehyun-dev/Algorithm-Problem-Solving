import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
for i in combinations([*range(1, n + 1)], m):
    for j in i:
        print(j, end=" ")
    print()