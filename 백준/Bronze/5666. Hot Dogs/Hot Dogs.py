import sys
for line in sys.stdin:
    H, P = map(int, line.split())
    print(format(round(H/P, 2), ".2f"))