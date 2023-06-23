import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    print(math.floor((-1 + math.sqrt(1 + 4 * int(input()))) / 2))