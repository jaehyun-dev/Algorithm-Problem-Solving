R, B = map(int, input().split())
t = R + B
for i in range(1, int(t ** (1 / 2)) + 2):
    j = (R + B) / i
    if j == int(j) and 2 * (i + j - 2) == R:
        print(int(j), i)
        break