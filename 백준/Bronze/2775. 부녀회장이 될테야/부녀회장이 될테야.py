t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    arr = []
    floor = []
    for i in range(1, n + 1):
        floor.append(i)
    arr.append(floor)

    for i in range(1, k + 1):
        floor = []
        count = 0
        for l in range(n):
            count += arr[i - 1][l]
            floor.append(count)
        arr.append(floor)

    print(arr[k][n - 1])