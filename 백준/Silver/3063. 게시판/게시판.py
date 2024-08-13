T = int(input())
for _ in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    p1 = (x2 - x1) * (y2 - y1)
    if x3 < x1:
        xl = x1
    elif x1 <= x3 < x2:
        xl = x3
    else:
        xl = x2
    if x2 < x4:
        xr = x2
    elif x1 < x4 <= x2:
        xr = x4
    else:
        xr = x1
    if y3 < y1:
        yd = y1
    elif y1 <= y3 < y2:
        yd = y3
    else:
        yd = y2
    if y2 < y4:
        yu = y2
    elif y1 < y4 <= y2:
        yu = y4
    else:
        yu = y1
    p2 = (xr - xl) * (yu - yd)
    print(p1 - p2)