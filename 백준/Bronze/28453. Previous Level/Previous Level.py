N = int(input())
a = list(map(int, input().split()))
for i in range(N):
    b = a[i]
    if b == 300:
        print(1, end=" ")
    elif b >= 275:
        print(2, end=" ")
    elif b >= 250:
        print(3, end=" ")
    else:
        print(4, end=" ")