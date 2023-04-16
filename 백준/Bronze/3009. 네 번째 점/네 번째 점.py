co_x = []
co_y = []
for _ in range(3):
    x, y = map(int, input().split())
    co_x.append(x)
    co_y.append(y)
co_x.sort()
co_y.sort()
print(co_x[0] if co_x.count(co_x[0]) == 1 else co_x[2], end= " ")
print(co_y[0] if co_y.count(co_y[0]) == 1 else co_y[2])