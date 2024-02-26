N = int(input())
if 5 < N:
    print("Love is open door")
else:
    a = int(input())
    for _ in range(N - 1):
        if a:
            print(0)
        else:
            print(1)
        a = not a