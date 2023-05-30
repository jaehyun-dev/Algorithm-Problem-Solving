n = int(input())
for i in range(1, n + 1):
    a = sorted(list(map(int, input().split())))
    print(f"Scenario #{i}:")
    print("yes" if ((a[2] ** 2) == (a[0] ** 2) + (a[1] ** 2)) else "no")
    print()