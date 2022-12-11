import sys
for line in sys.stdin:
    a, b = map(int, line.strip().split())
    if a == 0 and b == 0:
        break
    print("Yes") if a > b else print("No")