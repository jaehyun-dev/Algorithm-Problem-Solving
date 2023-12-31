N = int(input())
l = []
for _ in range(N):
    s = input()
    r = ord(s[0]) - 65
    c = int(s[1:]) - 1
    l.append((r, c))
a = [["." for _ in range(20)] for _ in range(10)]
for r, c in l:
    a[r][c] = "o"
for i in range(10):
    for j in range(20):
        print(a[i][j], end="")
    print()