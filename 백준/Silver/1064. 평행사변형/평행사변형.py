x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
x = set([x_a, x_b, x_c])
y = set([y_a, y_b, y_c])
point = [(x_a, y_a), (x_b, y_b), (x_c, y_c)]

def slope(a, b):
    return (b[1] - a[1]) / (b[0] - a[0])

def length(a, b):
    return ((((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) ** (1 / 2))

if len(x) == 1 or len(y) == 1:
    print(-1)
elif len(x) == 3 and slope(point[0], point[1]) == slope(point[0], point[2]):
    print(-1)
else:
    side = [length(point[0], point[1]), length(point[0], point[2]), length(point[1], point[2])]
    side.sort()
    diff = side[2] - side[0]
    print(2 * diff)