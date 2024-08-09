N, M = map(int, input().split())
J = int(input())
l, r = 1, M
cnt = 0
for _ in range(J):
    p = int(input())
    dl = l - p
    dr = p - r
    if 0 < dl:
        cnt += dl
        l -= dl
        r -= dl
    elif 0 < dr:
        cnt += dr
        l += dr
        r += dr
print(cnt)