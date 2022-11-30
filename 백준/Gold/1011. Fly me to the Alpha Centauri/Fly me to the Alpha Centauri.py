n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    distance = b - a
    move = 0
    j = 1
    count = 0

    while move < distance:
        i = 0
        while i < 2:
            move += j
            i += 1
            count += 1
            if move >= distance:
                break
        j += 1

    print(count)