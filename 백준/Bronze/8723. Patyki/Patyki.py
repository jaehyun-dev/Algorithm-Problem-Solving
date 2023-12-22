a = sorted(list(map(int, input().split())))
if a[0] == a[1] == a[2]:
    print(2)
elif a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
    print(1)
else:
    print(0)