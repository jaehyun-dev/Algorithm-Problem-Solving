while 1:
    a = list(map(int, input().split()))
    if set(a) == set([0]):
        break
    if a[2] - a[1] == a[1] - a[0]:
        print(f"AP {2 * a[2] - a[1]}")
    else:
        print(f"GP {int(a[2] ** 2 / a[1])}")