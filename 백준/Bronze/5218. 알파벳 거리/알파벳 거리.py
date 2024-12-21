T = int(input())
for _ in range(T):
    a, b = input().split()
    print("Distances: ", end="")
    for i in range(len(a)):
        x = ord(a[i])
        y = ord(b[i])
        if x <= y:
            print(y - x, end=" ")
        else:
            print(y + 26 - x, end=" ")
    print()