import math
import sys
input = sys.stdin.readline
while 1:
    n = input().strip()
    if n == '0':
        break
    a = 0
    for i in range(1, len(n) + 1):
        a += (int(n) % 10) * math.factorial(i)
        n = n[:-1]
    print(a)