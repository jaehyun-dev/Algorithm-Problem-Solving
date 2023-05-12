while 1:
    a = list(map(int, input().split()))
    if set(a) == {0}:
        break
    a.sort()
    if len(set(a)) == 1:
        print("Equilateral")
    elif a[0] + a[1] <= a[2]:
        print("Invalid")
    elif len(set(a)) == 2:
        print("Isosceles")
    else:
        print("Scalene")