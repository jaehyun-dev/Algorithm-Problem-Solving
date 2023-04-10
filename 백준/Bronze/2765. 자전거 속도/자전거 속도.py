import sys
PI = 3.1415927
inch = 1
feet = 12 * inch
M = 5280 * feet

i = 1
for line in sys.stdin:
    d, r, t = map(float, line.split())
    if r == 0:
        break
    distance = d * PI * r / M
    mph = distance / t * 3600
    print(f"Trip #{i}: {format(round(distance, 2), '.2f')} {format(round(mph, 2), '.2f')}")
    i += 1