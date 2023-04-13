def solution(dots):
    for i in range(3):
        l = list(dots)
        a = l.pop(0)
        b = l.pop(i)
        c = l.pop(0)
        d = l.pop(0)
        if slope(a, b) == slope(c, d):
            return 1
    return 0

def slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        return 'v'
    if x1 < x2:
        return (y2 - y1) / (x2 - x1)
    else:
        return (y1 - y2) / (x1 - x2)