ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
a = [[ds, ys], [dm, ym]]
if ys - ds > ym - dm:
    first = 0
    second = 1
else:
    first = 1
    second = 0
cur_1 = a[first][1] - a[first][0]
cur_2 = a[second][1] - a[second][0]
while 1:
    while cur_1 > cur_2:
        cur_2 += a[second][1]
    while cur_1 < cur_2:
        cur_1 += a[first][1]
    if cur_1 == cur_2:
        break
print(cur_1)