while 1:
    N = list(map(int, list(input())))
    if N == [0]:
        break
    while len(N) > 1:
        N = list(map(int, list(str(sum(N)))))
    print(N[0])