n, r, c = map(int, input().split())
score = [[0, 0], [0, 1], [1, 0], [1, 1]]
ans = 0
while r > 0 or c > 0:
    share_r = r // (2 ** (n - 1))
    share_c = c // (2 ** (n - 1))
    ans += score.index([share_r, share_c]) * ((2 ** (n - 1)) ** 2)
    r -= (2 ** (n - 1)) * share_r
    c -= (2 ** (n - 1)) * share_c
    n -= 1
print(ans)