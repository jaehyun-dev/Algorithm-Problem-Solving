T = int(input())
for _ in range(T):
    L, R, S = map(int, input().split())
    dl = S - L
    dr = R - S
    if dr <= dl:
        print(2 * dr)
    else:
        print(2 * dl + 1)