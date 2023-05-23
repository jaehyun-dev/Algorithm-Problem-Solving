while 1:
    N = int(input())
    if not N:
        break
    count = 0
    for i in range(1, N + 1):
        count += (N - i + 1) ** 2
    print(count)