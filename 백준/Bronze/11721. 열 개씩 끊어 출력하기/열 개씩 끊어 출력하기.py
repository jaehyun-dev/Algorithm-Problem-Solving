a = input()
i = 0
while i < len(a):
    print(a[i], end="")
    if i % 10 == 9:
        print()
    i += 1