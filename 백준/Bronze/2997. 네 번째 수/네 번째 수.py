a = list(map(int, input().split()))
a.sort()
b, c = a[1] - a[0], a[2] - a[1]
if b == c:
    print(a[2] + c)
elif b == 2 * c:
    print(a[0] + c)
else:
    print(a[1] + b)