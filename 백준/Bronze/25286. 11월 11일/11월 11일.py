c = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for _ in range(T):
    y, m = map(int, input().split())
    m = (m - 2) % 12 + 1
    d = c[m - 1]
    if m == 2 and ((y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)):
            d += 1
    if m == 12:
        y -= 1
    print(y, m, d)