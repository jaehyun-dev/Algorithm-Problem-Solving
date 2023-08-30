from itertools import combinations as comb
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    min_dif = sum(sum(arr, []))
    for i in comb(range(N), N // 2):
        a = 0
        b = 0
        j = tuple(set(range(N)) - set(i))
        for k in comb(i, 2):
            a += arr[k[0]][k[1]]
            a += arr[k[1]][k[0]]
        for l in comb(j, 2):
            b += arr[l[0]][l[1]]
            b += arr[l[1]][l[0]]
        dif = abs(a - b)
        min_dif = min(dif, min_dif)
    print(f"#{t} {min_dif}")