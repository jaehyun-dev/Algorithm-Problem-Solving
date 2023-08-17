import sys
for line in sys.stdin:
    A, B, C = map(int, line.split())
    print(max(C - B, B - A) - 1)