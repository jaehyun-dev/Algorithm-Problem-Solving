a = list(map(int, input().split()))
a.sort()
if a[0] + a[1] == a[2]:
    print(1)
elif a[0] * a[1] == a[2]:
    print(2)
else:
    print(3)