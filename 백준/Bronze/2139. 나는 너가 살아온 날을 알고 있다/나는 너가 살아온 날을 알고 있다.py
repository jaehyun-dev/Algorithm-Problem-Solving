a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(2, 12):
    a[i] = a[i - 1] + a[i]
while 1:
    d, m, y = map(int, input().split())
    if (d, m, y) == (0, 0, 0):
        break
    ans = a[m - 1] + d
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        if 2 < m:
            ans += 1
    print(ans)