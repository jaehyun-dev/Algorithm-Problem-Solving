n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            print("Dead", end="")
        if i % 5 == 0:
            print("Man")
        else:
            print()
    else:
        print(i, end=" ")