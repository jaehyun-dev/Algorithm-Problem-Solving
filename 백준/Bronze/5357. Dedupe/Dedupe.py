n = int(input())
for _ in range(n):
    a = input()
    print(a[0], end="")
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            print(a[i], end="")
    print()