N = int(input())
for _ in range(N):
    s, n = input().split("-")
    sv = 0
    for i in range(3):
        sv += (ord(s[i]) - 65) * (26 ** (2 - i))
    nv = int(n)
    v = abs(sv - nv)
    if 100 < v:
        print("not ", end="")
    print("nice")